from django.urls import path
from . import views

prefix = "code_"  # 设置前缀

urlpatterns = [
    path('', views.blog_list, name=prefix+"blog_list"),
    path("<int:id>", views.blog_article, name=prefix+"blog_article"),
    path("list_<int:id>", views.blog_category, name=prefix+"blog_category"),
]