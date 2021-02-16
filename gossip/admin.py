from django.contrib import admin
from .models import Gossip
# Register your models here.
@admin.register(Gossip)
class GossipAdmin(admin.ModelAdmin):
    list_display = ("id", "body", "created_time", "author")
    list_per_page = 20
    ordering = ("id",)
    list_display_links = ("body",)    # 打开链接的字段
    # fields = ("title","body")    # 在修改页面显示的字段数