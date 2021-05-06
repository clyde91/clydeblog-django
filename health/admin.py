from django.contrib import admin
from .models import MyHealth, Run


@admin.register(MyHealth)
class MyHealthAdmin(admin.ModelAdmin):
    list_display = ("id", "weight", "record_date")
    list_per_page = 20
    ordering = ("-record_date",)
    list_display_links = ("weight",)    # 打开链接的字段
    # fields = ("title","body")    # 在修改页面显示的字段数


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    list_display = ("id", "distance", "time", "record_date")
    list_per_page = 20
    ordering = ("-record_date",)
    list_display_links = ("distance",)    # 打开链接的字段
    # fields = ("title","body")    # 在修改页面显示的字段数