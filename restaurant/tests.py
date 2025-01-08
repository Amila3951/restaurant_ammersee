from django.test import TestCase
from django.urls import reverse
from .models import Reservation
from .forms import ReservationForm
from django.core import mail
from django.contrib.auth.models import User
from unittest.mock import patch

class MakeReservationViewTest(TestCase):
    def test_make_reservation_valid_form(self):
        data = {'date': '2024-12-31', 'time': '18:00', 'num_people': 2}
        form = ReservationForm(data=data)
        self.assertTrue(form.is_valid())
        print(form.errors)

        response = self.client.post(reverse('restaurant:make_reservation'), data)

        self.assertEqual(Reservation.objects.count(), 1)

        self.assertEqual(response.status_code, 302)



class SignupEmailTest(TestCase):

    @patch('emailjs.send')  # Mock the emailjs.send function
    def test_email_sent_on_signup(self, mock_send):
        """
        Test that EmailJS is called correctly when a user signs up.
        """
        # Create a new user
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        # Simulate form submission (this will call the sendEmail function)
        with self.client.as_user(user):
            response = self.client.post('/accounts/signup/', {
                'username': 'testuser',
                'email': 'testuser@example.com',
                'password': 'testpassword',
            })

        # Check if emailjs.send was called with the correct arguments
        mock_send.assert_called_once_with(
            'service_ab2vrqc',  # Your Service ID
            'template_oo7qvf5',  # Your Template ID
            {
                'to_email': 'testuser@example.com',
                'username': 'testuser'
            }
        )

        # Check if the user was redirected to the home page
        self.assertEqual(response.status_code, 302)  # 302 is the redirect status code
        self.assertEqual(response.url, '/')  # '/' is the home page URL