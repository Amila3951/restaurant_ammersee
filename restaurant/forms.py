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
        fields = [
            "name",
            "email",
            "phone",
            "date",
            "time",
            "num_people",
        ]  # Fields to include in the form
        widgets = {  # Customize the widgets for some fields
            "date": forms.DateInput(  # Use a date picker for the date field
                attrs={
                    "type": "date",
                    "class": "datepicker",
                },
                format="%Y-%m-%d",  # Specify the date format
            ),
            "time": forms.TimeInput(
                attrs={"type": "time"}
            ),  # Use a time picker for the time field
            "email": forms.EmailInput(
                attrs={}
            ),  # Use a default email input
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Enter your phone number",
                    "pattern": r"^\+?\d{9,15}$",
                }
            ),
        }

    def clean_date(self):
        """
        Custom validation for the date field to ensure it's not in the past.
        """
        date = self.cleaned_data[
            "date"
        ]  # Get the date from the cleaned data
        today = date.today()  # Get today's date
        tomorrow = today + timedelta(days=1)  # Calculate tomorrow's date
        if (
            date < tomorrow
        ):  # Check if the selected date is before tomorrow
            raise forms.ValidationError(
                "Reservation date cannot be in the past or on the current day."
            )  # Raise an error if the date is invalid
        return date  # Return the validated date


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form to include the email field.
    """

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # Explicitly get the User model
        fields = UserCreationForm.Meta.fields + (
            "email",
        )  # Add email to the list of fields
