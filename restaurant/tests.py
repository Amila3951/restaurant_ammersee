from django.test import TestCase
from .models import Reservation
from .forms import ReservationForm
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta


class MakeReservationViewTest(TestCase):

    def test_make_reservation_valid_form(self):
        """
        Test that a valid reservation form creates a new reservation.
        """
        # Generate a date in the future for the reservation
        today = timezone.now().date()
        tomorrow = today + timedelta(days=1)
        data = {
            'date': tomorrow.strftime('%Y-%m-%d'),  # Format the date as YYYY-MM-DD
            'time': '18:00', 
            'num_people': 2,
            'name': 'Test User',  # Add a name
            'email': 'test@example.com',  # Add an email
            'phone': '1234567890'  # Add a phone number
        }

        form = ReservationForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)  # Check if the form is valid, print errors if not

        response = self.client.post(reverse('restaurant:make_reservation'), data)  # Simulate a POST request

        self.assertEqual(Reservation.objects.count(), 1)  # Check if one reservation was created
        self.assertEqual(response.status_code, 302)  # Check for redirect status code (302)

    def test_make_reservation_invalid_form(self):
        """
        Test that an invalid reservation form does not create a new reservation.
        """
        # Create data for the form with an invalid date (in the past)
        today = timezone.now().date()
        yesterday = today - timedelta(days=1)
        data = {
            'date': yesterday.strftime('%Y-%m-%d'),  # Format the date as YYYY-MM-DD
            'time': '18:00', 
            'num_people': 2,
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '1234567890'
        }

        form = ReservationForm(data=data)
        self.assertFalse(form.is_valid())  # Check if the form is invalid

        response = self.client.post(reverse('restaurant:make_reservation'), data)  # Simulate a POST request

        self.assertEqual(Reservation.objects.count(), 0)  # Check that no reservations were created
        self.assertEqual(response.status_code, 200)  # Expect the same page to be rendered with errors (status code 200)


