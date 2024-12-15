from . import views as reservation_views  # Import views from the current app as 'reservation_views'
from django.urls import path  # Import the path function for defining URL patterns
from . import views  # Import all views from the current app
from django.contrib.auth import views as auth_views  # Import authentication views from Django
from .views import MyLoginView  # Import the custom login view

app_name = 'restaurant'  # Set the application namespace

urlpatterns = [
    path('', reservation_views.home, name='home'),  # Home page URL
    path('menu/', views.menu, name='menu'),  # Menu page URL
    path('make/', views.make_reservation, name='make_reservation'),  # Make a reservation URL
    path('confirmation/', views.reservation_confirmation, name='reservation_confirmation'),  # Reservation confirmation URL 
    path('my_reservations/', views.my_reservations, name='my_reservations'),  # My reservations page URL
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),  # Edit reservation URL
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),  # Delete reservation URL
    path('accounts/login/', MyLoginView.as_view(), name='account_login'),  # Login URL using the custom view
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='restaurant:home'), name='account_logout'),  # Logout URL with redirect to home
    path('confirmation/<int:reservation_id>/', views.reservation_confirmation, name='reservation_confirmation')  # Reservation confirmation URL
]