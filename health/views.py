from django.shortcuts import render
from health.models import MyHealth

def myhealth():
    data = MyHealth.objects.order_by("record_date")
    time = []
    weight = []
    for info in data:
        time.append(info.record_date.strftime("%Y-%m-%d"))
        weight.append(float(info.weight))
    context = {}
    context['time'] = time
    context['weight'] = weight
    return context