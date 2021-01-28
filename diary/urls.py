from django.urls import path
from . import views


urlpatterns = [
    path('', views.diary_list, name="diary_list"),
    path("<int:id>", views.diary_article, name="diary_article"),
]