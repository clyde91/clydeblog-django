from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.urls import reverse    # 反向解析
from .forms import LoginForm, RegForm
from django.contrib.auth.models import User


def index(request):
    apps = ["blog","architecture"]
    context = {}
    context['apps'] = apps
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def test(request):
    context = {}
    return render(request, "test.html", context)


def login(request):
    '''
    username = request.POST['username']     # POST大写
    password = request.POST['password']
    user = auth.authenticate(request, username=username,password=password)
    referer = request.META.get('HTTP_REFERER', reverse('home'))    # 获得跳转前的网站。如果没有则后者  referer“反向解析”home在的地址
    if user is not None:
        auth.login(request, user)
        return redirect(referer)
    else:
        return render(request, 'error.html', {"message":'用户名或密码不正确'})
    '''
    if request.method == 'POST':  #加判断login这个方法是打开登录页面的处理，还是提交登录数据的请求。相当于2个方法合并到一个来。
        login_form = LoginForm(request.POST)  #将post传来的数据实例化成表单
        if login_form.is_valid():
            user = login_form.cleaned_data["user"]
            auth.login(request, user)
            return redirect(request.GET.get("from", reverse('home')))

    else:
        login_form = LoginForm()  # request方法不是POST

    context = {}  # if分支的共有部分，都会执行以下代码。
    context['login_form'] = login_form
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            # 登录用户
            user = auth.authenticate(request, username=username,password=password)
            auth.login(request, user)
            return redirect(request.GET.get("from", reverse('home')))

    else:
        reg_form = RegForm()  #request方法不是POST时

    context = {}  #if分支的共有部分，都会执行以下代码。
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)