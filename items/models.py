from django.db import models

class Category(models.Model):
    """ A class to display the category """

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class BrandOrAuthor(models.Model):
    """ A class to display the Brand or Author of the product"""
    brand = models.CharField(max_length=25, null=True, blank=True)
    

    def __str__(self):
        return self.brand

class Colour(models.Model):
    """ A class to display the colour of the product """
    colour = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.colour

class ClothesType (models.Model):
    """ A class to display the clothing type """
    clothes = models.CharField(max_length=25, null=True, blank=True)
    
    def __str__(self):
        return self.clothes

class Size(models.Model):
    """ A class to display the size of the product """
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size

class KidsAge(models.Model):
    """ A class to display the age range of the product """
    kids_age = models.CharField(max_length=50)

    def __str__(self):
        return self.kids_age

MEN_WOMEN_CHILDREN = [
    ('na', 'N/A'),
    ('men', 'Men'),
    ('women', 'Women'),
    ('children', 'Children')
]

class Item(models.Model):
    """ A class to record each product Item """
    
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    clothes_type = models.ForeignKey('ClothesType', null=True, blank=True, on_delete=models.SET_NULL)
    men_women_children = models.CharField(max_length=200, choices=MEN_WOMEN_CHILDREN, default='na')
    size = models.ForeignKey('Size', null=True, blank=True, on_delete=models.SET_NULL)
    kids_age = models.ForeignKey('KidsAge', null=True, blank=True, on_delete=models.SET_NULL)
    colour = models.ForeignKey('Colour', null=True, blank=True, on_delete=models.SET_NULL)
    brand_or_author = models.ForeignKey('BrandOrAuthor', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quality = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name
