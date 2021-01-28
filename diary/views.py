from django.shortcuts import render,get_object_or_404
from .models import Diary
from django.core.paginator import Paginator
from django.conf import settings
from common_func.utils import read_click, paginate
from django.contrib.contenttypes.fields import ContentType
from comment.models import Comment

# Create your views here.
def diary_article(request, id):
    article = get_object_or_404(Diary, id=id)
    key=read_click(request, obj=article)
    context = {}
    context['article'] = article
    context['object_id'] = id
    content_type = ContentType.objects.get_for_model(article)
    comments = Comment.objects.filter(content_type=content_type, object_id=id)
    context['comments'] = comments
    context['content_type'] = "article"    # 传入模型的名字。这里存在疑问。如果不同app有相同的article该怎么办
    response = render(request,"diary_detail.html", context)    # 响应
    response.set_cookie(key, max_age=1200,)    # 给字典赋值真
    return response


def diary_list(request):
    context = {}
    articles_all = Diary.objects.all()
    paginate(request,articles_all=articles_all,context=context)    # 分页器
    context['articles'] = articles_all
    return render(request, "diary_list.html", context)