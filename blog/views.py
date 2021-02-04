from django.shortcuts import render,get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator
from django.conf import settings
from common_func.utils import read_click, paginate
from django.contrib.contenttypes.fields import ContentType
from comment.models import Comment
from comment.forms import CommentForm
#from common_func.models import WebSEO
# Create your views here.


def blog_article(request, id):
    article = get_object_or_404(Article, id=id)  #通过content_type和id获得的obj
    key=read_click(request, obj=article)
    context = {}
    context['article'] = article
    context['object_id'] = id
    content_type = ContentType.objects.get_for_model(article)  # 用具体的obj来获得content_type
    comments = Comment.objects.filter(content_type=content_type, object_id=id, parent=None)  #只筛选根评论
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={"content_type":content_type.model, "object_id":id, "reply_comment_id":"0"})  # 实例化一个form表单。content_type.model这个.model很关键不然会出错

    #context["test"] = content_type.model_class  # 测试专用
    context["now_category"] = article.category  # 获得当前文章的category
    context["now_categorys"] = Category.objects.all()  # 当前所有分类
    context['url_name'] = "blog_article"
    context['prefix'] = ""

    #context['content_type'] = "article"    # 传入模型的名字。这里存在疑问。如果不同app有相同的article该怎么办？= ContentType.objects.get_for_model(article)行不行

    # webseos = WebSEO.objects.filter(content_type=content_type, object_id=id)
    #for i in webseos:
    #    webseo1 = i
    #context['webseo'] = webseo1 #外挂seo的信息
    response = render(request,"article_detail.html", context)    # 响应
    response.set_cookie(key, max_age=1200,)    # 给字典赋值真
    return response


def blog_list(request):
    context = {}
    articles_all = Article.objects.all()
    paginate(request,articles_all=articles_all,context=context)    # 分页器
    context['articles'] = articles_all
    context['url_name'] = "blog_article"

    context["now_categorys"] = Category.objects.all()  # 当前所有分类
    return render(request, "article_list.html", context)


def blog_category(request, id):
    context = {}
    category = get_object_or_404(Category,id=id)    #通过id=id获取分类的实例（当前category）
    articles_category = Article.objects.filter(category=id)    #用分类筛选后的文章
    paginate(request,articles_all=articles_category,context=context)    # 分页器
    context["articles"] = articles_category
    context['url_name'] = "blog_article"  # 如何通过自生寻找url

    context["now_category"] = category
    context["now_categorys"] = Category.objects.all()  # 当前所有分类
    return render(request, "article_category.html", context)

