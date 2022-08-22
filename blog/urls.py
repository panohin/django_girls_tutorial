from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list_url'),
]