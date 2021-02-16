from django.shortcuts import render
from common_func.utils import paginate
from .models import Gossip

# Create your views here.
def gossip_list(request):
    context = {}
    gossip_all = Gossip.objects.all()
    paginate(request,articles_all=gossip_all,context=context)    # 分页器
    context['gossips'] = gossip_all

    return render(request, "gossip_list.html", context)