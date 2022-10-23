
from django.contrib import admin
from .models import (
    Category, BrandOrAuthor, Colour, ClothesType, Size, KidsAge, Item)


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'clothes_type',
        'size',
        'kids_age',
        'colour',
        'brand_or_author',
        'description',
        'price',
        'quality',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(BrandOrAuthor)
admin.site.register(Colour)
admin.site.register(ClothesType)
admin.site.register(Size)
admin.site.register(KidsAge)
admin.site.register(Item, ItemAdmin)
