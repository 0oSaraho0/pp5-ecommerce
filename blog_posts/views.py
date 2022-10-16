from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost    


class BlogPostList(ListView):
    """ A view to return a list of blog posts"""
    model = BlogPost
    queryset = BlogPost.objects.order_by('created_on')
    template_name = 'blog_posts/blog_posts.html'
    paginate_by = 6

