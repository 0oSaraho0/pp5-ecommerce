from django.db import models


class BlogPost(models.Model):
    """ A model to create a blog post """
    charity_name = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200)
    donation_amount = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True, default='placeholder')
    summary = models.TextField(blank=True)
    charity_location = models.CharField(max_length=200, unique=False)
    charity_website = models.URLField(
        max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.event_name
