from . import views as reservation_views 
from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views 
from .views import MyLoginView, AddReservationView, DeleteReservationView, EditReservationView
import importlib
import sys

app_name = 'restaurant' 


urlpatterns = [
    path('home', reservation_views.home, name='home'),
    path('menu/', views.menu, name='menu'),  
    path('make/', views.make_reservation, name='make_reservation'),  
    path('my_reservations/', views.my_reservations, name='my_reservations'),  
    path('my_reservations/<int:reservation_id>/edit/', views.edit_reservation, name='edit_reservation'),  
    path('my_reservations/<int:reservation_id>/delete/', views.delete_reservation, name='delete_reservation'), 
    path('accounts/login/', MyLoginView.as_view(), name='account_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='restaurant:home'), name='account_logout'),
    path('confirmation/<int:reservation_id>/', views.reservation_confirmation, name='reservation_confirmation'), 

    # Admin URLs
    path('admin/reservations/', views.admin_reservations, name='admin_reservations'),
    path('admin/reservations/add/', AddReservationView.as_view(), name='add_reservation'),
    path('admin/reservations/<int:pk>/edit/', views.EditReservationView.as_view(), name='admin_edit_reservation'),  
    path('admin/reservations/<int:pk>/delete/', views.DeleteReservationView.as_view(), name='admin_delete_reservation'), 
]