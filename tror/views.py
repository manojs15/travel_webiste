from django.shortcuts import render, redirect,get_object_or_404
from .forms import TravelBookingForm
from .models import TravelBooking
from django.contrib.auth.decorators import user_passes_test

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
def order_details(request, order_id):
    # Retrieve the order object from the database
    order = get_object_or_404(TravelBooking, pk=order_id)

    # Pass the order object to the template
    return render(request, 'order_details.html', {'order': order})