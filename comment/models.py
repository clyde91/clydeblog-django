from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import ContentType
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)    #评论所属的ct
    object_id = models.PositiveIntegerField()    # 在app里的id
    content_object = GenericForeignKey('content_type', "object_id")    # 评论的实例
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="评论人")

    class Meta:
        verbose_name_plural = "评论"
        ordering = ['-created_time']






