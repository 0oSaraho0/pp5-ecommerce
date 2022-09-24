from django.shortcuts import render
from .models import Item

# Create your views here.
def all_items(request):
    """ A view to show all products including sorting and search queries """

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render (request, 'items/items.html', context)
