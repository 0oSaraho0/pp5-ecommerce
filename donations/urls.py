from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('donations/', views.MakeDonation.as_view(), name='donations'),
    path(
        'donation_confirmation/',
        views.DonationConfirmation.as_view(),
        name='donation_confirmation'
    ),
]
