from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'blog_posts/',
        views.BlogPostList.as_view(),
        name='blog_posts'
    ),
    path(
        '<int:id>/',
        views.BlogPostDetailView.as_view(),
        name='blog_post_detail'
    ),
    path(
        'create/',
        views.BlogPostCreateView.as_view(),
        name='create_blog_post'
    ),
    path(
        'edit/<int:id>/',
        views.EditBlogPostView.as_view(),
        name='edit_blog_post'
    ),
    path(
        'delete/<int:id>/',
        views.BlogPostDelete.as_view(),
        name='blog_post_delete'
    ),
]
