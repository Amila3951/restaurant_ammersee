from . import views as reservation_views 
from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views 
from .views import MyLoginView   

app_name = 'restaurant'  

urlpatterns = [
    path('admin/reservations/', views.admin_reservations, name='admin_reservations'),
    path('home', reservation_views.home, name='home'),  # URL for the home page
    path('menu/', views.menu, name='menu'),  # URL for the menu page
    path('make/', views.make_reservation, name='make_reservation'),  # URL for making a reservation
    path('my_reservations/', views.my_reservations, name='my_reservations'),  # URL for viewing user's reservations
    path('my_reservations/<int:reservation_id>/edit/', views.edit_reservation, name='edit_reservation'),  # URL for editing a reservation
    path('my_reservations/<int:reservation_id>/delete/', views.delete_reservation, name='delete_reservation'),  # URL for deleting a reservation
    path('accounts/login/', MyLoginView.as_view(), name='account_login'),  # URL for the login page using a custom view
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='restaurant:home'), name='account_logout'),  # URL for logging out, redirects to home
    path('confirmation/<int:reservation_id>/', views.reservation_confirmation, name='reservation_confirmation'),  # URL for reservation confirmation
    
]