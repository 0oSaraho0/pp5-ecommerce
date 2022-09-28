from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Item, Category

# Create your views here.

def all_items(request):
    """ A view to show all products, including sorting and search queries """

    items = Item.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            items = items.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,"You didn't enter any searh criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            items = items.filter(queries)

    current_sorting = f'{sort}_{direction}'
            
    context = {
        'items': items,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,

    }

    return render(request, 'items/items.html', context)

def item_detail(request, item_id):
    """ A view to show individual item details """
    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)

