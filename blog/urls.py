from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    path("<int:id>", views.blog_article, name="blog_article"),
    path("list_<int:id>", views.blog_category, name="blog_category"),
]