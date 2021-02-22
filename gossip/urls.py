from django.urls import path
from . import views


urlpatterns = [
    path('', views.gossip_list, name="gossip_list"),
    path('gossip_index', views.gossip_index, name="gossip_index"),
    # path("<int:id>", views.blog_article, name="blog_article"),
    path('submit_gossip', views.submit_gossip, name="submit_gossip"),
]
