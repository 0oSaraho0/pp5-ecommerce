from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    """Form details to arrange a collection"""
    class Meta:
        model = Donation
        fields = ('full_name', 'email', 'phone_number', 'postcode',
                  'town_or_city', 'street_address1', 'street_address2',
                  'county', 'collection_date', 'donation_description',
                  'number_of_bags')
