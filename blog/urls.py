from django.contrib import admin
from django.urls import path, include
from . import views


# app_name = 'blog'
urlpatterns = [
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit_url'),
	path('post/new/', views.post_new, name='post_new_url'),
	path('<int:pk>', views.post_detail, name='post_detail_url'),
	path('', views.post_list, name='post_list_url'),
]