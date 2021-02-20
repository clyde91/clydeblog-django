from django.contrib import admin
from .models import MyHealth


@admin.register(MyHealth)
class MyHealthAdmin(admin.ModelAdmin):
    list_display = ("id", "weight", "record_date")
    list_per_page = 20
    ordering = ("id",)
    list_display_links = ("weight",)    # 打开链接的字段
    # fields = ("title","body")    # 在修改页面显示的字段数