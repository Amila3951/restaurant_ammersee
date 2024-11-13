from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'date',
            'time',
            'num_people',
            'first_name',
            'last_name',
            'email',
            'phone',
        ]