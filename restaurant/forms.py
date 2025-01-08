from django import forms
from .models import Reservation
from datetime import date, timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class ReservationForm(forms.ModelForm):
    """
    Form for creating and editing reservations.
    """
    class Meta:
        model = Reservation  # Use the Reservation model
        fields = ['name', 'email', 'phone', 'date', 'time', 'num_people'] 
        widgets = {  # Customize the widgets for some fields
            'date': forms.DateInput(  # Use a date picker for the date field
                attrs={
                    'type': 'date',
                    'class': 'datepicker', 
                    'placeholder': 'Select a date'
                },
                format='%Y-%m-%d'
            ),
            'time': forms.TimeInput(attrs={'type': 'time'}),  # Use a time picker for the time field
            'email': forms.EmailInput(attrs={}),  # Use a default email input
        }

    def clean_date(self):
        """
        Custom validation for the date field to ensure it's not in the past.
        """
        date = self.cleaned_data['date']
        today = date.today()
        tomorrow = today + timedelta(days=1)
        if date < tomorrow:
            raise forms.ValidationError("Reservation date cannot be in the past or on the current day.")
        return date


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form to include the email field.
    """
    email = forms.EmailField(required=True)  # Add email field and make it required

    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # Explicitly get the User model
        fields = UserCreationForm.Meta.fields + ('email',)  # Add email to the list of fields