
from .models import BlogPost
from django import forms


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
