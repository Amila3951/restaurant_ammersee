from django.urls import path
from . import views

urlpatterns = [
    path('make/', views.make_reservation, name='make_reservation'),
    path('success/', views.reservation_success, name='reservation_success'),
]