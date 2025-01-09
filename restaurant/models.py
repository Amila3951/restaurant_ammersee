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
    tomorrow = today + timedelta(days=1)  # Calculate tomorrow's date
    if value < tomorrow:
        raise ValidationError(
            "Reservation date cannot be in the past or on the current day."
        )


class Reservation(models.Model):
    """
    Model representing a table reservation.
    """

    time = models.TimeField(blank=False, null=False)  # Reservation time
    num_people = models.IntegerField(
        validators=[MinValueValidator(1)]  # Ensure the number of people is at least 1
    )
    name = models.CharField(max_length=200)  # Name of the person making the reservation
    email = models.EmailField(
        validators=[EmailValidator()], blank=True, null=True
    )  # Email address (optional)
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r"^\+?\d{9,15}$")],  # Validate phone number format
    )
    date = models.DateField(
        validators=[validate_future_date]
    )  # Reservation date (must be in the future)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,  # Link to the User model (optional)
    )

    def __str__(self):
        """
        String representation of the Reservation object.
        """
        return f"Reservation for {self.num_people} by {self.name} on {self.date} at {self.time}"

    def clean(self):
        """
        Additional validation to check if the reservation time is within
        the restaurant's opening hours.
        """
        opening_time = datetime.strptime("10:00", "%H:%M").time()  # Opening time
        closing_time = datetime.strptime("22:00", "%H:%M").time()  # Closing time

        if self.time < opening_time or self.time > closing_time:
            raise ValidationError("Reservation time must be between 10:00 and 22:00.")


class Dish(models.Model):
    """
    Model representing a dish on the menu.
    """

    CATEGORY_CHOICES = (  # Choices for the dish category
        ("appetizer", "Appetizer"),
        ("main", "Main Course"),
        ("dessert", "Dessert"),
        ("drink", "Drink"),
    )
    name = models.CharField(max_length=255)  # Name of the dish
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price of the dish
    category = models.CharField(
        max_length=200, default="Main Courses"
    )  # Category of the dish

    def __str__(self):
        """
        String representation of the Dish object.
        """
        return self.name
