from django.urls import path, include
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("data/", views.data, name="data"),
    path("get_ajax/", views.get_ajax, name="get_ajax"),
    path("fun_change/", views.fun_change, name="fun_change"),
]
