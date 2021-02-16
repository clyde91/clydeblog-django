from django.shortcuts import render,get_object_or_404,redirect
from common_func.utils import paginate
from .models import Gossip
from django.contrib.contenttypes.models import ContentType
from gossip.forms import GossipForm
from django.urls import reverse


# Create your views here.
def gossip_list(request):
    context = {}
    gossip_all = Gossip.objects.all()
    paginate(request,articles_all=gossip_all,context=context)    # 分页器
    context['gossips'] = gossip_all
    context['gossip_form'] = GossipForm()  # 实例化一个form表单。
    return render(request, "gossip_list.html", context)


def submit_gossip(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    # 数据检查
    user = request.user

    if not user.is_authenticated:
        author_id = 2
    else:
        author_id = user.id
    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, "error.html", {'message': '内容为空', 'redirect_to': referer})
    # 检查通过，保持
    gossip = Gossip()
    gossip.author_id = author_id
    gossip.text = text
    gossip.save()
    return redirect(referer)