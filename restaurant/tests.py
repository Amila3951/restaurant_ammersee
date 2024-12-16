from django.test import TestCase
from django.urls import reverse
from .models import Reservation
from .forms import ReservationForm

class MakeReservationViewTest(TestCase):
    def test_make_reservation_valid_form(self):
        data = {'date': '2024-12-31', 'time': '18:00', 'num_people': 2}
        form = ReservationForm(data=data)
        self.assertTrue(form.is_valid())
        print(form.errors)

        response = self.client.post(reverse('restaurant:make_reservation'), data)

        self.assertEqual(Reservation.objects.count(), 1)

        self.assertEqual(response.status_code, 302)
