from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_bag(request):
    """ A view to render the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, bag_item_id):
    """ Add  item to bag """

    quantity = 1
    
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if bag_item_id in list(bag.keys()):
        messages.error(request, "The requested quantity is not available")
    else:
        bag[bag_item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, bag_item_id):
    """ Remove item from bag """
    
    bag = request.session.get('bag', {})
    bag.pop(bag_item_id)

    request.session['bag'] = bag
    messages.success(request, "{{item.item.name}} has been successfully removed")
    return redirect(reverse('view_bag'))

