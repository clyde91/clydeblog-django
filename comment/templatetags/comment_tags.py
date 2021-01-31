from django import template
from django.contrib.contenttypes.fields import ContentType
from comment.models import Comment

register = template.Library()  # 注意L大写

@register.simple_tag
def test():
    return "test code"

@register.simple_tag
def get_comment_num(obj):  # 传入的obj很关键只要传入obj就能得到评论数
    content_type = ContentType.objects.get_for_model(obj)  # 根据传入的obj来获取contenttype
    return Comment.objects.filter(content_type=content_type, object_id=obj.id).count()  # 返回评论数