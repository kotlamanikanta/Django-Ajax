from django.urls import path, include
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("data/", views.data, name="data"),
]
