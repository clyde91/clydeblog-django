from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.contenttypes.fields import ContentType
from django.urls import reverse
# Create your views here.


def submit_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    # 数据检查
    user = request.user
    if not user.is_authenticated:
        return render(request, "error.html", {'message': '用户未登录', 'redirect_to': referer})    # 返回链接为之前页
    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, "error.html", {'message': '评论内容为空', 'redirect_to': referer})
    try:
        content_type = request.POST.get('content_type', '')    # 这些数据都是通过request获得
        object_id = int(request.POST.get('object_id', ''))
        content_object = ContentType.objects.get(model=content_type).model_class().objects.get(id=object_id)
        # 通过模型的名字这里是article，获得ct。然后ct的方法.model_class获得模型，这里是Article。然后get再获得实例。
    except Exception as e:
        return render(request, "error.html", {'message': '评论对象不存在', 'redirect_to': referer})

    # 检查通过，保持
    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = content_object
    comment.save()
    return redirect(referer)
