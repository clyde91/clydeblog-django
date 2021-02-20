from django.contrib import admin
from .models import Gossip


@admin.register(Gossip)
class GossipAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_time", "author")
    list_per_page = 20
    ordering = ("id",)
    list_display_links = ("text",)    # 打开链接的字段
    # fields = ("title","body")    # 在修改页面显示的字段数