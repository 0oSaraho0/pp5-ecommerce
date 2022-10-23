from django.shortcuts import render
from .forms import ReviewForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from django.contrib import messages


class ReviewList(ListView):
    """ A view to return a list of reviews"""
    model = Review
    queryset = Review.objects.order_by('-created_on')
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'


class CreateReview(LoginRequiredMixin, CreateView):
    """A view to write a review"""

    model = Review
    form_class = ReviewForm
    success_url = '/reviews/reviews/'
    template_name = 'reviews/create_review.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Post created successfully')
        return super(CreateReview, self).form_valid(form)
