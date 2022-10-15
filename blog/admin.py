from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


@admin.register(Post)
class BlogAdmin(SummernoteModelAdmin):
    """ A class to display Blog items on admin """

    list_display = ('event_name', 'created_on')
    search_fields = ['event_name', 'content']
    list_filter = ('created_on',)
    summernote_fields = ('content')