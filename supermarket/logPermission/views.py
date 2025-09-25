from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import marketuser

# Create your views here.

def login_view(request):
    if request.method == "POST":
        user_id = request.POST['userid']
        password = request.POST['password']

        try:
            user = marketuser.objects.get(user_id=user_id)
        except marketuser.DoesNotExist:
            messages.error(request, "该账户不存在，请重新输入")
            return redirect("login")

        if user.password == password:
            request.session['password'] = user.password
            request.session['user_id'] = user.user_id
            request.session['user_name'] = user.user_name
            if user.role == "管理员":
                return redirect("admin_dashboard")
            if user.role == "销售员":
                return redirect("sales_dashboard")
            if user.role == "采购员":
                return redirect("purchase_dashboard")
            if user.role == "库存管理员":
                return redirect("admin_dashboard.html")
        else:
            messages.error(request, "密码错误，请重新输入")
            return redirect("login")

    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        user_id=request.POST['userid'];
        user_name=request.POST['username'];
        role=request.POST['role'];
        password=request.POST['password'];
        phone=request.POST['phone'];

        marketuser.objects.create(
            user_id=user_id,
            user_name=user_name,
            role=role,
            password=password,
            phone=phone,
        )

        return redirect("login")

    return render(request, "register.html")



def logout_view(request):
    logout(request)  # 注销用户登录状态
    return redirect('login')  # 重定向到登录页面


