from django.contrib import admin
from .models import BlogPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class BlogIdeaAdmin(SummernoteModelAdmin):
    """ A class to display blog posts on admin """

    list_display = ('event_name', 'created_on')
    search_fields = ['event_name', 'charity_name', 'content']
    list_filter = ('created_on',)
    summernote_fields = ('content')
