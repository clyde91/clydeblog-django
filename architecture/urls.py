from django.urls import  path
from . import views


urlpatterns = [
    path('',views.architecture_list,name="architecture_list"),
    path("<int:id>", views.architecture_detail, name="architecture_detail"),
    path("s<id>", views.test, name="test"),
]