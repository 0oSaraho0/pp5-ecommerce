from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog_posts/', views.BlogPostList.as_view(), name='blog_posts'),
    path('<int:id>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),



    
]