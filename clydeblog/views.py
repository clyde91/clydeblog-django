from django.shortcuts import render, redirect
from django.urls import reverse    # 反向解析
from gossip.models import Gossip
from arch_blog.models import ArchBlog
from django.core.mail import send_mail


def index(request):
    context = {}
    context['archblogs'] = ArchBlog.objects.order_by("-created_time")[:6]
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def test(request):
    context = {}
    context['gossip'] = Gossip.objects.filter(author_id=1).order_by("-created_time")[:10]
    return render(request, "test.html", context)


def contact_me(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    send_mail(subject, "姓名："+name+"\r\n邮箱："+email+"\r\n内容："+message, '66704470@qq.com',
    ['66704470@qq.com'], fail_silently=False)
    return redirect(referer)
