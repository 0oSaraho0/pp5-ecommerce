
from .models import BlogPost
from django import forms
# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class BlogPostForm(forms.ModelForm):
    """ A form to create an idea """
    class Meta:
        model = BlogPost
        fields = (
            'event_name',
            'charity_name',
            'image',
            'donation_amount',
            'charity_website',
            'summary',
        )
        # widgets = {
        #     'review': SummernoteWidget()
        # }