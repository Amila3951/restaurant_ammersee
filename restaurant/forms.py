from django import forms
from .models import Reservation
from datetime import date, timedelta

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'num_people']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'datepicker',
                    'placeholder': 'Select a date'
                },
                format='%Y-%m-%d'
            ),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        today = date.today()
        tomorrow = today + timedelta(days=1)
        if date < tomorrow:
            raise forms.ValidationError("Reservation date cannot be in the past or on the current day.")
        return date