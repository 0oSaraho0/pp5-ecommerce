from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    """ A class to display Donations requests on admin """

    list_display = ('full_name', 'donation_description', 'number_of_bags')
    search_fields = ['full_name', 'number_of_bags']
    list_filter = ('full_name', 'number_of_bags')
