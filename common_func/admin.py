from django.contrib import admin
from .models import Readnum #, WebSEO
# Register your models here.


@admin.register(Readnum)
class ReadnumAdmin(admin.ModelAdmin):
    list_display = ("id", "content_object", "read_num", "content_type", "object_id")
    ordering = ("id",)
    list_display_links = ("content_type",)

# @admin.register(WebSEO)
# class WebSEOAdmin(admin.ModelAdmin):
#     list_display = ("id", "content_object", "keywords", "descriptison", "content_type", "object_id")
#     ordering = ("id",)
#     list_display_links = ("content_object",)
#     # fields = ("keywords", "descriptison", "content_type", "object_id") #在修改页面显示哪些字段