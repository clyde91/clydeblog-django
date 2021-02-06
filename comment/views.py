from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .forms import CommentForm
from django.http import JsonResponse
# Create your views here.


def submit_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST, user=request.user)  # 用post传来的数据实例化一个表单
    data = {}

    if comment_form.is_valid():
        # 检查通过，保存数据
        comment = Comment()    # 实例化一个评论
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']

        parent = comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()

        # 返回数据
        data['status'] = 'SUCCESS'
        data['username'] = comment.user.username
        data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%M:%S')
        data['text'] = comment.text
        if not parent is None:
            data['reply_to'] = comment.reply_to.username
        else:
            data['reply_to'] = ''
        data['id'] = comment.id
        data['root_id'] = comment.root.id if not comment.root is None else ''
    else:
        #return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)








'''
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
        model_class = ContentType.objects.get(model=content_type).model_class()
        content_object = model_class.objects.get(id=object_id)
        # 通过模型的名字的字符串这里是'article'，获得ct。然后ct的方法.model_class获得模型，这里是Article。然后get再获得实例。
    except Exception as e:
        return render(request, "error.html", {'message': '评论对象不存在', 'redirect_to': referer})

    # 检查通过，保持
    comment = Comment()  # 在数据库新建个评论
    comment.user = user
    comment.text = text
    comment.content_object = content_object
    comment.save()
    return redirect(referer)
'''



'''
def submit_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST, user=request.user)  # 通过post实例提交的表单。多传一个user。
    data = {}
    if comment_form.is_valid():
        comment = Comment()  # 在数据库新建个评论
        comment.user = comment_form.cleaned_data["user"]  # 也可以是request.user。统一一点
        comment.text = comment_form.cleaned_data["text"]
        comment.content_object = comment_form.cleaned_data["content_object"]  #值为这条评论所属的文章实例
        comment.save()
        # 返回数据
        data['status'] = 'SUCCESS'
        data['username'] = comment.user.username
        data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%M:%S')
        data['text'] = comment.text
        #return redirect(referer)
    else:
        #return render(request, "error.html", {'message': comment_form.errors, 'redirect_to': referer})
        data["status"] = "ERROR"
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)
'''


'''    referer = request.META.get('HTTP_REFERER', reverse('home'))
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
        model_class = ContentType.objects.get(model=content_type).model_class()
        content_object = model_class.objects.get(id=object_id)
        # 通过模型的名字的字符串这里是'article'，获得ct。然后ct的方法.model_class获得模型，这里是Article。然后get再获得实例。
    except Exception as e:
        return render(request, "error.html", {'message': '评论对象不存在', 'redirect_to': referer})

    # 检查通过，保持
    comment = Comment()  # 在数据库新建个评论
    comment.user = user
    comment.text = text
    comment.content_object = content_object
    comment.save()
    return redirect(referer)
'''

