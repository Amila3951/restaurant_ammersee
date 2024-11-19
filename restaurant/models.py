from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, EmailValidator, RegexValidator
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User  # Django's built-in User model


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

    date = models.DateField(
        validators=[validate_future_date]
    )  # Date of the reservation
    time = models.TimeField()  # Time of the reservation
    num_people = models.IntegerField(
        validators=[MinValueValidator(1)]
    )  # Number of people (must be at least 1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(
        max_length=20, validators=[RegexValidator(r"^\+?\d{9,15}$")]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
        """
        Additional validation to check if the reservation time is within
        the restaurant's opening hours.
        """
        opening_time = datetime.strptime("10:00", "%H:%M").time()  # Opening time
        closing_time = datetime.strptime("22:00", "%H:%M").time()  # Closing time
        if not (opening_time <= self.time <= closing_time):
            raise ValidationError("Reservation time must be between 10:00 and 22:00.")

    def __str__(self):
        return f"Reservation for {self.num_people} on {self.date} at {self.time}"


class Dish(models.Model):
    """
    Model representing a dish on the menu.
    """

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
