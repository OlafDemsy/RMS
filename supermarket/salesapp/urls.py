from django.urls import path
from . import views


urlpatterns = [
    path('sales/dashboard/', views.sales_dashboard, name='sales_dashboard'),
    path("sales/records/create/", views.sales_records_create, name='sales_records_create'),
    path('sales/records/list/', views.sales_records_list, name='sales_records_list'),
    path('sales/record/list/<int:sales_record_id>/', views.sales_record_detail, name='sales_record_detail'),
    path('sales/profit/summary/', views.sales_profit_summary, name='sales_profit_summary'),
]