from common_func.models import Readnum
from django.contrib.contenttypes.fields import ContentType
from django.core.paginator import Paginator
from django.conf import settings


# 点击添加数量
def read_click(request, obj):
    ct = ContentType.objects.get_for_model(obj)  # 获得ct
    key = "%s_%s_read" % (ct.model, obj.id)
    if not request.COOKIES.get(key):
        if Readnum.objects.filter(content_type=ct, object_id=obj.id).count():    # 判断是否有数。没有为0假
            readnum = Readnum.objects.get(content_type=ct, object_id=obj.id)
        else:
            readnum = Readnum(content_type=ct, object_id=obj.id)    # 这里是实体。
        readnum.read_num += 1
        readnum.save()    # 保存的是实体不是实体内的属性。
    return key


# 分页器
def paginate(request,articles_all,context):    # 传入的：articles_all需要分页的文章，context字典
    paginator = Paginator(articles_all,settings.NUM_ARTICLE_PER_PAGE)  # 每8页分页
    page_num = request.GET.get('page',1)  # get获取页码
    page = paginator.get_page(page_num)  # 当前页
    nav_page_range = [x for x in range(int(page_num)-2, int(page_num)+3) if 0 < x <= paginator.num_pages]  # 前后各2个。如果前面取到小于1就取1。后面取到最后页码就取最后页码
    # 加首页尾页省略号
    if nav_page_range[0] != 1:
        nav_page_range.insert(0,1)
        if nav_page_range[1]-1>=2:
            nav_page_range.insert(1, '...')
    if nav_page_range[-1] != paginator.num_pages:
        nav_page_range.append(paginator.num_pages)
        if paginator.num_pages-nav_page_range[-2] >= 2:
            nav_page_range.insert(-1, '...')
    context['page'] = page
    context['page_num'] = page_num
    context['nav_page_range'] = nav_page_range


