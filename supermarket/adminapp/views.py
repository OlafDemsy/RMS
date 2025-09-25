from django.shortcuts import render, redirect, get_object_or_404
from logPermission.models import marketuser
from django.contrib import messages
# Create your views here.

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def employee_list(request):
    employees = marketuser.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        user_id = request.POST['userid']
        user_name = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        phone = request.POST['phone']

        marketuser.objects.create(
            user_id=user_id,
            user_name=user_name,
            password=password,
            role=role,
            phone=phone,)

        return redirect('admin_dashboard')

    return render(request, 'employee_add.html')

def employee_edit(request, user_id):
    employee = get_object_or_404(marketuser, user_id=user_id)

    if request.method == 'POST':
        employee.user_id = request.POST.get('user_id')
        employee.user_name = request.POST.get('username')
        employee.phone = request.POST.get('phone')
        employee.role = request.POST.get('role')
        password = request.POST.get('password')
        if password:
            employee.password = password

        employee.save()
        return redirect('employee_list')

    return render(request, 'employee_edit.html', {'employee': employee})





def employee_delete(request, user_id):
    employee = get_object_or_404(marketuser, pk=user_id)

    if request.method == 'POST':
        employee.delete()
        messages.success(request, "员工已成功删除")
        return redirect('employee_list')

    # 如果非 POST 请求，直接重定向或抛 405 错误
    return redirect('employee_list')

