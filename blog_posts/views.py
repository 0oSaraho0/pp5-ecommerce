from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
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


class BlogPostCreateView(CreateView):
    """ A view to create an idea """

    form_class = BlogPostForm
    template_name = 'blog_posts/create_blog_post.html'
    success_url = "/blog_posts/blog_posts/"
    model = BlogPost

    def form_valid(self, form):
        """ If form is valid return to browse ideas """

        messages.success(self.request, 'Blog post created successfully')
        return super(BlogPostCreateView, self).form_valid(form)


class EditBlogPostView(UpdateView):
    """ A view to edit an idea """

    Model = BlogPost
    form_class = BlogPostForm
    success_url = "/blog_posts/blog_posts/"
    template_name = "blog_posts/edit_blog_post.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)

    def form_valid(self, form):
        """ If form is valid return to browse ideas """
        messages.success(self.request, 'Idea created successfully')
        return super().form_valid(form)


class BlogPostDelete(DeleteView):
    """ A view to delete an idea """
    model = BlogPost
    success_url = "/blog_posts/blog_posts/"
    template_name = "blog_posts/blog_post_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)
