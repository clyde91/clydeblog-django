from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from common_func.models import ReadnumMethod


class Diary(models.Model, ReadnumMethod):
    title = models.CharField(max_length=70, verbose_name="标题")
    body = RichTextUploadingField(verbose_name="正文")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改日期")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")

    def __str__(self):
        return '<%s>' % self.title  # 设置后台显示默认模型信息

    class Meta:
        verbose_name_plural = "日志"
        ordering = ['-created_time']


class Private(models.Model, ReadnumMethod):
    title = models.CharField(max_length=70, verbose_name="标题")
    body = RichTextUploadingField(verbose_name="正文")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改日期")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")

    def __str__(self):
        return '<%s>' % self.title  # 设置后台显示默认模型信息

    class Meta:
        verbose_name_plural = "私密日志"
        ordering = ['-created_time']