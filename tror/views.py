from django.shortcuts import render, redirect,get_object_or_404
from .forms import TravelBookingForm
from .models import TravelBooking
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseBadRequest


def success_view(request):
    if request.method == 'POST':
        form = TravelBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tror:done')
    else:
        form = TravelBookingForm()
    return render(request, 'ordform.html', {'form': form})

def ord_form(request):
    form = TravelBookingForm()
    return render(request, 'ordform.html', {'form': form})

def done_view(request):
    return render(request, 'success.html')

@user_passes_test(lambda u: u.is_superuser)
def order_details(request):
    # Retrieve all orders from the database
    orders = TravelBooking.objects.all()

    # Pass the orders to the template
    return render(request, 'order_details.html', {'orders': orders})


def update_order(request):
    if request.method == 'POST':
        # Check if delete_order button is clicked
        if 'delete_order' in request.POST:
            # Get the order ID to delete
            order_id_to_delete = request.POST['delete_order']
            # Delete the order
            order_to_delete = get_object_or_404(TravelBooking, pk=order_id_to_delete)
            order_to_delete.delete()
        else:
            # Get the list of completed order IDs from the form
            completed_orders = request.POST.getlist('completed_orders')
            # Retrieve all orders
            orders = TravelBooking.objects.all()
            # Iterate through all orders
            for order in orders:
                # If the order ID is in completed_orders list, mark it as completed
                if str(order.id) in completed_orders:
                    order.completed = True
                else:
                    # If the order ID is not in completed_orders list, mark it as not completed
                    order.completed = False
                order.save()  # Save the changes to the database
    else:
        # If the request method is not POST, retrieve all orders
        orders = TravelBooking.objects.all()
        return render(request, 'order_details.html', {'orders': orders})
    # Redirect back to the order details page
    return redirect('tror:order_details')