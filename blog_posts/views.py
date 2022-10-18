from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SuperuserRequiredMixin
from django.contrib import messages
from .models import BlogPost 
from .forms import BlogPostForm   


class BlogPostList(ListView):
    """ A view to return a list of blog posts"""
    model = BlogPost
    queryset = BlogPost.objects.order_by('created_on')
    template_name = 'blog_posts/blog_posts.html'
    paginate_by = 6


class BlogPostDetailView(DetailView):
    """ A view to see the blog post details"""
    model = BlogPost
    template_name = 'blog_posts/blog_post_detail.html'
    queryset = BlogPost.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)


class BlogPostCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    """ A view to create an idea """

    form_class = BlogPostForm
    template_name = 'blog_posts/create_blog_post.html'
    success_url = "/blog_posts/blog_posts/"
    model = BlogPost

    def form_valid(self, form):
        """ If form is valid return to browse ideas """
        form.instance.superuser = self.request.superuser
        messages.success(self.request, 'Idea created successfully')
        return super(BlogPostCreateView, self).form_valid(form)
