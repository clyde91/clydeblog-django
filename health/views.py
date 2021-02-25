from health.models import MyHealth
from django.http import JsonResponse


def myhealth(request):
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
    return JsonResponse(data)
