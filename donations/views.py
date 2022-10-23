from django.shortcuts import render
from .models import Donation
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from .forms import DonationForm


class MakeDonation(CreateView):
    """A view to make a donation"""

    model = Donation
    form_class = DonationForm
    success_url = '/donations/donation_confirmation/'
    template_name = 'donations/donations.html'

    def form_valid(self, form):
        messages.success(
            self.request, 'Collection request successfully recieved.'
            'Thank you for your donation')
        return super(MakeDonation, self).form_valid(form)


class DonationConfirmation(TemplateView):
    """
    View to render donataion collection confirmation
    """
    template_name = 'donations/donation_confirmation.html'
