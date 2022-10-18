from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost    


class BlogPostList(ListView):
    """ A view to return a list of blog posts"""
    model = BlogPost
    queryset = BlogPost.objects.order_by('created_on')
    template_name = 'blog_posts/blog_posts.html'
    paginate_by = 6


class BlogPostDetailView(DetailView):

    model = BlogPost
    template_name = 'blog_posts/blog_post_detail.html'
    queryset = BlogPost.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)
