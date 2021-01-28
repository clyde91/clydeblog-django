from django.contrib import admin
from .models import Comment
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "user", "created_time", "content_type", "object_id", "content_object")
    list_per_page = 20
    ordering = ("id",)
    list_display_links = ("text",)
    # fields = ("title","body")    #修改页面显示内容