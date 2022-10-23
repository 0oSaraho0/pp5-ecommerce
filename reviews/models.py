from django.db import models


class Review(models.Model):
    """ A model to create a blog post """
    title = models.CharField(max_length=200, null=True)
    user = models.CharField(max_length=200)
    review = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ Order by created on date """
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.review} by {self.user}"
