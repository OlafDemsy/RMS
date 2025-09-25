from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from decimal import Decimal
from .models import Customers, Products, SalesRecords
from logPermission.models import marketuser
from django.db import connection
# Create your views here.

def sales_dashboard(request):
    user_name = request.session.get('user_name')
    return render(request, 'sales_dashboard.html', {"user_name": user_name})

def sales_records_create(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        customer_name = request.POST['customer_name']
        sales_quantity = int(request.POST['sales_quantity'])

        product = get_object_or_404(Products, product_name=product_name)
        customer = get_object_or_404(Customers, customer_name=customer_name)
        user_id = request.session['user_id']
        user = get_object_or_404(marketuser, user_id=user_id)

        if product.product_quantity is None or product.product_quantity < sales_quantity:
            return HttpResponse("库存不足，无法销售")

        sales_price = product.sales_price
        sales_total_price = sales_price * sales_quantity
        product.product_quantity -= sales_quantity
        product.save()

        SalesRecords.objects.create(
            user=user,
            customer=customer,
            product=product,
            sales_quantity=sales_quantity,
            sales_total_price=sales_total_price,
        )

        return redirect('sales_dashboard')

    return render(request, 'sales_records_create.html')


def sales_records_list(request):
        sales_records = SalesRecords.objects.select_related('user', 'product').all()

        return render(request, 'sales_records_list.html', {'sales_records': sales_records})

def sales_record_detail(request, sales_record_id):
    sales_record = get_object_or_404(SalesRecords.objects.select_related('user', 'product', 'customer'), pk=sales_record_id)
    return render(request, 'sales_records_detail.html', {'sales_record': sales_record})



def sales_profit_summary(request):
    with connection.cursor() as cursor:
        cursor.callproc('calculate_sales_summary')
        result = cursor.fetchall()

    # 一般只有一行结果
    summary = {
        'total_sales': result[0][0] or 0,
        'total_cost': result[0][1] or 0,
        'total_profit': result[0][2] or 0
    }

    return render(request, 'sales_profit_summary.html', {'summary': summary})
