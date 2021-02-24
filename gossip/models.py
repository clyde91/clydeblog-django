from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Gossip(models.Model):
    # title = models.CharField(max_length=70, verbose_name="标题")
    text = RichTextUploadingField(verbose_name="文本")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    # tag = models.ManyToManyField(Tag, blank=True, verbose_name="标签")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")  # 通过author_id反链

    def __str__(self):
        return '<%s>' % self.text  # 设置后台显示默认模型信息

    class Meta:
        verbose_name_plural = "说说"
        ordering = ['-created_time']

    # def get_absolute_url(self):  # 获得自己文章的url
    #     from django.urls import reverse
    #     return reverse(prefix+'blog_article', args=(self.id,))
