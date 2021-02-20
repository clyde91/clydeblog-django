from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.urls import reverse    # 反向解析
from .forms import LoginForm, RegForm
from django.contrib.auth.models import User
from gossip.models import Gossip
from arch_blog.models import ArchBlog
from health.views import myhealth
from django.core.mail import send_mail


def index(request):
    apps = ["blog","architecture"]
    health = myhealth()
    context = {}
    context['apps'] = apps
    context['gossip'] = Gossip.objects.filter(author_id=1).order_by("-created_time")[:2]
    context['archblogs'] = ArchBlog.objects.order_by("-created_time")[:6]
    context['time'] = health["time"]
    context['weight'] = health["weight"]
    context['weight_max'] = max(health["weight"])
    context['weight_min'] = min(health["weight"])-5
    return render(request, "index.html", context)


def about(request):
    healths = MyHealth.objects.all()
    dic = {}
    for i in healths:
        dic[i.record_date] = i.weight
    context = {}
    context['data'] = dic.keys()
    context['record_date'] = dic.values()
    return render(request, "about.html", context)


def test(request):
    context = {}
    return render(request, "test.html", context)


def login(request):
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


def logout(request):  #退出登录
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    auth.logout(request)
    return redirect(referer)



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


def contact_me(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    send_mail(subject, "姓名："+name+"\r\n邮箱："+email+"\r\n内容："+message, '66704470@qq.com',
    ['66704470@qq.com'], fail_silently=False)
    return redirect(referer)


