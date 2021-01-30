from django.urls import path
from . import views


urlpatterns = [
    path('', views.code_blog_list, name="code_blog_list"),
    path("<int:id>", views.code_blog_article, name="code_blog_article"),
    path("list_<int:id>", views.code_blog_category, name="code_blog_category"),
]