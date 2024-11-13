from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, EmailValidator, RegexValidator
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User


def validate_future_date(value):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    if value < tomorrow:
        raise ValidationError(
        )


class Reservation(models.Model):
    date = models.DateField(validators=[validate_future_date])
    time = models.TimeField()
    num_people = models.IntegerField(validators=[MinValueValidator(1)])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(
        max_length=20, validators=[RegexValidator(r"^\+?\d{9,15}$")]
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    def clean(self):
        opening_time = datetime.strptime("10:00", "%H:%M").time()
        closing_time = datetime.strptime("22:00", "%H:%M").time()
        if not (opening_time <= self.time <= closing_time):
            raise ValidationError(
            )

    def __str__(self):
        return f"Reservation for {self.num_people} on {self.date} at {self.time}"


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name