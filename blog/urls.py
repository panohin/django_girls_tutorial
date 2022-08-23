from django.contrib import admin
from django.urls import path, include
from . import views


# app_name = 'blog'
urlpatterns = [
	path('<int:pk>', views.post_detail, name='post_detail_url'),
	path('', views.post_list, name='post_list_url'),
]