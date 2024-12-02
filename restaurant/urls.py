from . import views as reservation_views
from django.urls import path
from . import views 

app_name = 'restaurant'

urlpatterns = [
    path('', reservation_views.home, name='home'),  
    path('menu/', views.menu, name='menu'),
    path('make/', views.make_reservation, name='make_reservation'),
    path('register/', views.register, name='register'),
    path('confirmation/', views.reservation_confirmation, name='reservation_confirmation'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]