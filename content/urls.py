from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('connect/', views.connect, name="connect"),
    path('partnerships/', views.partnerships, name="partnerships"),
]
