from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('make/', views.make_reservation, name='make_reservation'),
    path('menu/', views.menu, name='menu'),
    path('register/', views.register, name='register'),
    path('confirmation/', views.reservation_confirmation, name='reservation_confirmation'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('make/', views.make_reservation, name='make_reservation'),
]