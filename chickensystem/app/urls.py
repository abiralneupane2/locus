from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="user"),
    path("user/", views.realTimeData, name="user"),
    path("input/", views.input, name="input")
]