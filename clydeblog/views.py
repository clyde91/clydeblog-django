#from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.contrib import auth
from django.urls import reverse    # 反向解析
#from django.contrib.auth.models import User
from gossip.models import Gossip
from arch_blog.models import ArchBlog
from health.models import MyHealth
from health.views import myhealth
from django.core.mail import send_mail
#import json


def index(request):
    apps = ["blog","architecture"]
    #health = myhealth(request)
    context = {}
    context['apps'] = apps
    context['gossip'] = Gossip.objects.filter(author_id=1).order_by("-created_time")[:2]
    context['archblogs'] = ArchBlog.objects.order_by("-created_time")[:6]

    myhealth = MyHealth.objects.order_by("record_date")
    time = []
    weight = []
    for info in myhealth:
        time.append(info.record_date.strftime("%Y-%m-%d"))
        weight.append(float(info.weight))
    data = {}
    data['time'] = time
    data['weight'] = weight
    data['weight_max'] = max(weight)
    data['weight_min'] = min(weight)-5
    context['health'] = data
    #context['time'] = health["time"]
    #context['weight'] = health["weight"]
    #context['weight_max'] = max(health["weight"])
    #context['weight_min'] = min(health["weight"])-5
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def test(request):
    context = {}
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
