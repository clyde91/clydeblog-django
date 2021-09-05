from health.models import MyHealth, Run
from django.http import JsonResponse
import time


# def myhealth(request):
#     myhealth = MyHealth.objects.order_by("record_date")
#     time = []
#     weight = []
#     for info in myhealth:
#         time.append(info.record_date.strftime("%Y-%m-%d"))
#         weight.append(float(info.weight))
#     data = {}
#     data['time'] = time
#     data['weight'] = weight
#     data['weight_max'] = max(weight)
#     data['weight_min'] = min(weight)-5
#     return JsonResponse(data)

def str_data_to_num(str_data):
    # 格式时间成毫秒
    strptime = time.strptime(str_data, "%Y-%m-%d")
    mktime = int(time.mktime(strptime)*1000)
    return mktime


def num_to_str_data(str_data):
    str_data = str_data/1000
    # 格式毫秒成指定格式时间
    str_data = time.localtime(str_data)  # 生成一个元祖式的时间
    print(str_data)
    strptime = time.strftime("%Y-%m-%d", str_data) #格式化元祖
    print("strptime",strptime)


def myhealth(request):
    myhealth = MyHealth.objects.order_by("record_date")
    health = []
    weight = []
    # time = []
    for info in myhealth:
        message = []
        message.append(str_data_to_num(info.record_date.strftime("%Y-%m-%d")))
        message.append(float(info.weight))
        # time.append(info.record_date.strftime("%Y-%m-%d"))
        weight.append(float(info.weight))
        health.append(message)
    data = {}
    # data['time'] = time
    data['health'] = health
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

