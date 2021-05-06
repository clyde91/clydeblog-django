from health.models import MyHealth, Run
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


def run(request):
    run = Run.objects.order_by("record_date")
    time = []
    date = []
    distance = []
    speed = []
    for info in run:
        date.append(info.record_date.strftime("%Y-%m-%d"))
        dis = float(info.distance)
        tim = float(info.time)
        rtime = (tim-int(tim))*100/60+int(tim)  # 转小数
        spd = rtime/dis  # 计算
        stime = round((spd-int(spd))*60/100, 2)+int(spd)  # 转秒数

        distance.append(dis)
        time.append(tim)
        speed.append(stime)
    data = {}
    data['distance'] = distance
    data['time'] = time
    data['date'] = date
    data['speed'] = speed
    data['speed_max'] = max(speed)
    data['speed_min'] = min(speed)-1
    return JsonResponse(data)

