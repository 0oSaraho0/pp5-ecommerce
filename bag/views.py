from django.shortcuts import render, redirect
from django.contrib import messages


def view_bag(request):
    """ A view to render the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_bag_id):
    """ Add  item to bag """

    quantity = 1
    
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_bag_id in list(bag.keys()):
        messages.error(request, "The requested quantity is not available")
    else:
        bag[item_bag_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)