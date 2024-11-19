from django.urls import path
from . import views

urlpatterns = [
    path('make/', views.make_reservation, name='make_reservation'),
    path('menu/', views.menu, name='menu'),
    path('register/', views.register, name='register'),
    path('confirmation/', views.reservation_confirmation, name='reservation_confirmation'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
]