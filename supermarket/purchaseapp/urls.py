from django.urls import path
from . import views

urlpatterns = [
    path('purchase/dashboard/', views.purchase_dashboard, name='purchase_dashboard'),
    path('purchase/records/create/', views.purchase_records_create, name='purchase_records_create'),
    path('purchase/records/list/', views.purchase_records_list, name='purchase_records_list'),
    path('purchase/records/list/<int:purchase_record_id>/', views.purchase_records_detail, name='purchase_record_detail'),
    path('inventory/warning/', views.low_inventory_warning, name='low_inventory_warning'),

]