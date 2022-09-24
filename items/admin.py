from django.contrib import admin
from .models import Category, BrandOrAuthor, Colour, ClothesType, Size, KidsAge, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'clothes_type',
        'men_women_children'
        'size',
        'kids_age',
        'colour',
        'brand_or_author',
        'description',
        'price',
        'quality',
        'image',    
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Category)
admin.site.register(BrandOrAuthor)
admin.site.register(Colour)
admin.site.register(ClothesType)
admin.site.register(Size)
admin.site.register(KidsAge)
admin.site.register(Item)

