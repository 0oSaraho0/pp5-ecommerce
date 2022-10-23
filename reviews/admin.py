from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ A class to display a review items admin """

    list_display = ('user', 'title', 'review', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('user', 'title', 'review')
