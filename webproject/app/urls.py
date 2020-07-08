
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.function,name='home'),
    path('upload', views.uploadImage, name='uploadimage'),
]
