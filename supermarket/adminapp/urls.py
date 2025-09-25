from django.urls import path
from . import views


urlpatterns = [
    path('adminapp/', views.admin_dashboard, name='admin_dashboard'),
    path('employee/list/', views.employee_list, name='employee_list'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/edit/<int:user_id>/', views.employee_edit, name='employee_edit'),
    path('employees/<int:user_id>/delete/', views.employee_delete, name='employee_delete'),
]