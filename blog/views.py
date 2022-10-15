from django.shortcuts import render
from .models import Post


class PostList(ListView):
    """ A view to return a list of ideas"""
    model = Post
    queryset = Post.objects.order_by('created_on')
    template_name = 'blog/blog_posts.html'
    paginate_by = 6
