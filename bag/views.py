from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from items.models import Item


def view_bag(request):
    """ A view to render the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, bag_item_id):
    """ Add  item to bag """

    item = get_object_or_404(Item, pk=bag_item_id)
    quantity = 1

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if bag_item_id in list(bag.keys()):
        messages.error(request, f"The requested quantity is not available")
    else:
        bag[bag_item_id] = quantity
        messages.success(request, f"Added {item.name} to your bag")

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, bag_item_id):
    """ Remove item from bag """

    item = get_object_or_404(Item, pk=bag_item_id)
    bag = request.session.get('bag', {})
    bag.pop(bag_item_id)

    request.session['bag'] = bag
    messages.success(request, f"{item.name} has been successfully removed")
    return redirect(reverse('view_bag'))
