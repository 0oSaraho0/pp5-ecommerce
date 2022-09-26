from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def all_items(request):
    """ A view to show all products, including sorting and search queries """

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'items/items.html', context)

def item_detail(request, item_id):
    """ A view to show individual item details """
    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)

