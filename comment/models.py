from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import ContentType
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)    # 评论所属的ct
    object_id = models.PositiveIntegerField()    # 在app里的id
    content_object = GenericForeignKey('content_type', "object_id")    # 评论的实例
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    user = models.ForeignKey(User, related_name="comments", on_delete=models.DO_NOTHING, verbose_name="评论人")
    # 指定user与comment链接是"comments"。即调用obj.user与obj.reply_to。同样都是链接User的数据他内部能区分开来

    root = models.ForeignKey("self", related_name="root_comments", null=True, on_delete=models.DO_NOTHING)
    # 设置评论所属的根评论。精髓。利用当前obj.root_comments可以找到所有root相同的评论
    parent = models.ForeignKey("self", related_name="parent_comments", null=True, on_delete=models.DO_NOTHING)
    # 允许为空（最顶级没有父亲时为空）利用parent=none可以筛选所有根评论。有个问题。这2个好像重复了？obj.parent_comments难道不想？
    reply_to = models.ForeignKey(User, related_name="replies", null=True, on_delete=models.DO_NOTHING)
    # 回复的用户，如果是根评论则空

    class Meta:
        verbose_name_plural = "评论"
        ordering = ['-comment_time']

    def __str__(self):  # 当显示comment对象时改为显示comment.text的内容
        return self.text


# class Reply(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.DO_NOTHING)  # 设置外键。将回复与评论绑定
#




