from django.urls import path
from . import views


urlpatterns = [
    path('', views.myhealth, name="myhealth"),
    path('run', views.run, name="run"),
]