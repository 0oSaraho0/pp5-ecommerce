
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Donation(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    collection_date = models.DateTimeField(auto_now_add=False)
    donation_description = models.TextField(blank=True)
    number_of_bags = models.IntegerField(validators=[MinValueValidator(0),
                                         MaxValueValidator(50)])

    def __str__(self):
        return self.donation_description
