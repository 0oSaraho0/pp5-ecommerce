from django import forms
from .models import Donation
from django.contrib.admin import widgets 


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('full_name', 'email', 'phone_number', 'postcode',
                    'town_or_city', 'street_address1', 'street_address2',
                    'county', 'collection_date', 'donation_description',
                    'number_of_bags')

        widgets = {
            'collection_date': widgets.AdminSplitDateTime}

            
