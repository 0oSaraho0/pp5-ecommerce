from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """ A form to make a comment """
    class Meta:
        model = Review
        fields = ('title', 'review',)
