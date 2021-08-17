from django.contrib import admin
from .models import ArchBlog, Category, Tag
# Register your models here.


@admin.register(ArchBlog)
class ArchBlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_time", "modified_time", "get_read_num", "keywords", "description", "logo")
    list_per_page = 20
    ordering = ("-id",)
    list_display_links = ("title",)    # 打开链接的字段
    # fields = ("title","body")    # 在修改页面显示的字段数


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo", )
    ordering = ("id",)


admin.site.register(Tag)
