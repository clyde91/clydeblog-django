from django.contrib import admin
from .models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_time", "modified_time", "get_read_num", "private")
    list_per_page = 20
    ordering = ("id",)
    list_display_links = ("title",)    # 打开链接的字段
    # fields = ("title","body")    # 在修改页面显示的字段数
