from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory, Providers, PurchaseRecords
from salesapp.models import Products
from logPermission.models import marketuser
from django.db.models import F

# Create your views here.

def purchase_dashboard(request):
    user_name = request.session.get('user_name')
    return render(request,'purchase_dashboard.html', {"user_name":user_name})

def purchase_records_create(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        provider_name = request.POST['provider_name']
        purchase_quantity = int(request.POST['purchase_quantity'])
        inventory_places = request.POST['inventory_places']

        product = get_object_or_404(Products, product_id=product_id)
        provider = get_object_or_404(Providers, provider_name=provider_name)
        user_id = request.session['user_id']
        user = get_object_or_404(marketuser, user_id=user_id)

        stock, created = Inventory.objects.get_or_create(
            product=product,
            inventory_places=inventory_places,
            defaults={'inventory_quantity': 0}
        )

        stock.inventory_quantity += purchase_quantity
        stock.save()

        purchase_price = product.purchase_price
        purchase_total_price = purchase_price * purchase_quantity

        PurchaseRecords.objects.create(
            product=product,
            provider=provider,
            purchase_quantity=purchase_quantity,
            stock=stock,
            user=user,
            purchase_total_price=purchase_total_price
        )

        return redirect('purchase_dashboard')

    products = Products.objects.all()
    return render(request,'purchase_records_create.html', {"products":products})

def purchase_records_list(request):
    purchase_records = PurchaseRecords.objects.select_related('product', 'provider', 'stock').all()
    return render(request, "purchase_records_list.html", {"purchase_records":purchase_records})

def purchase_records_detail(request, purchase_record_id):
    purchase_record = get_object_or_404(PurchaseRecords.objects.select_related('user', 'product', 'provider', 'stock'), pk=purchase_record_id)
    return render(request, "purchase_records_detail.html", {"purchase_record":purchase_record})


def low_inventory_warning(request):
    # 查找库存低于阈值的记录
    low_inventory_items = Inventory.objects.filter(inventory_quantity__lt=F('reorder_threshold')).select_related('product')
    return render(request, 'low_inventory_warning.html', {'low_inventory_items': low_inventory_items})




