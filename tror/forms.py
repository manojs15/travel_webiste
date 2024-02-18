from django import forms
from .models import TravelBooking

class TravelBookingForm(forms.ModelForm):
    class Meta:
        model = TravelBooking
        fields = '__all__'
