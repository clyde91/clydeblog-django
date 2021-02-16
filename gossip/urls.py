from django.urls import path
from . import views


urlpatterns = [
    path('', views.gossip_list, name="gossip_list"),
    # path("<int:id>", views.blog_article, name="blog_article"),
]