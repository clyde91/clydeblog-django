from django.shortcuts import render,get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator
from django.conf import settings
from common_func.utils import read_click, paginate
from django.contrib.contenttypes.fields import ContentType
from comment.models import Comment
<<<<<<< HEAD
#from common_func.models import WebSEO
=======
from comment.forms import CommentForm
>>>>>>> 3d001a49d9538b2c37d8e725df782709d16a0aae
# Create your views here.


def blog_article(request, id):
    article = get_object_or_404(Article, id=id)
    key=read_click(request, obj=article)
    context = {}
    context['article'] = article
    context['object_id'] = id
    content_type = ContentType.objects.get_for_model(article)
    comments = Comment.objects.filter(content_type=content_type, object_id=id)
    context['comments'] = comments
    # webseos = WebSEO.objects.filter(content_type=content_type, object_id=id)
    #for i in webseos:
    #    webseo1 = i
    #context['webseo'] = webseo1 #外挂seo的信息
    context['content_type'] = "article"    # 传入模型的名字。这里存在疑问。如果不同app有相同的article该怎么办
    # 传入表单参数
    context['comment_form'] = CommentForm(initial={"content_type": content_type.model, "object_id": id})
    response = render(request, "article_detail.html", context)    # 响应
    response.set_cookie(key, max_age=1200,)    # 给字典赋值真
    return response


def blog_list(request):
    context = {}
    articles_all = Article.objects.all()
    paginate(request,articles_all=articles_all,context=context)    # 分页器
    context['articles'] = articles_all
    return render(request, "article_list.html", context)


def blog_category(request, id):
    context = {}
    category = get_object_or_404(Category, id=id)    #通过id=id获取分类的实例
    articles_category = Article.objects.filter(category=id)    #用分类筛选后的文章
<<<<<<< HEAD
    paginate(request,articles_all=articles_category,context=context)    # 分页器
=======
    paginate(request, articles_all=articles_category, context=context)    # 分页器
    categorys = Category.objects.all()
>>>>>>> 3d001a49d9538b2c37d8e725df782709d16a0aae
    context["articles"] = articles_category
    return render(request, "article_category.html", context)

