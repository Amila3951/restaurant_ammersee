from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, EmailValidator, RegexValidator
from datetime import date, datetime, timedelta
from django.conf import settings

def validate_future_date(value):
    """
    Custom validator to ensure that the reservation date is not in the past
    or on the current day.
    """
    today = date.today()
    tomorrow = today + timedelta(days=1) 
    if value < tomorrow:
        raise ValidationError(
            "Reservation date cannot be in the past or on the current day."
        )

class Reservation(models.Model):
    """
    Model representing a table reservation.
    """ 
    time = models.TimeField() 
    num_people = models.IntegerField(
        validators=[MinValueValidator(1)]  # Ensure the number of people is at least 1
    ) 
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()], blank=True, null=True)  # Allow blank email
    phone = models.CharField(
        max_length=20, validators=[RegexValidator(r"^\+?\d{9,15}$")]  # Validate phone number format
    )
    date = models.DateField(validators=[validate_future_date])  # Use the custom validator
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True  # Link to the User model
    )
    

    def __str__(self):
        return f"Reservation for {self.num_people} by {self.name} on {self.date} at {self.time}" 

    def clean(self):
        """
        Additional validation to check if the reservation time is within
        the restaurant's opening hours.
        """
        opening_time = datetime.strptime("10:00", "%H:%M").time()  # Opening time
        closing_time = datetime.strptime("22:00", "%H:%M").time()  # Closing time
        if not (opening_time <= self.time <= closing_time):
            raise ValidationError("Reservation time must be between 10:00 and 22:00.")


class Dish(models.Model):
    """
    Model representing a dish on the menu.
    """
    CATEGORY_CHOICES = (
        ('appetizer', 'Appetizer'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),  
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=200, default="Main Courses")

    def __str__(self):
        return self.name