from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """ A class to display a review items admin """

    list_display = ('user', 'title', 'review', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('user', 'title', 'review')