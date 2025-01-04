from django.urls import path, include
from restaurant import views as reservation_views
from django.contrib import admin

urlpatterns = [
    path('', reservation_views.home, name='home'), 
    path('restaurant/', include('restaurant.urls', namespace='restaurant_app')),
    path('admin/', admin.site.urls),
    path('my_reservations/', include('restaurant.urls', namespace='reservations')), 
    path('accounts/', include('allauth.urls')),
]