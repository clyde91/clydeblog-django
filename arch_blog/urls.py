from django.urls import path
from . import views


urlpatterns = [
    path('', views.arch_blog_list, name="arch_blog_list"),
    path("<int:id>", views.arch_blog_article, name="arch_blog_article"),
    path("list_<int:id>", views.arch_blog_category, name="arch_blog_category"),
]