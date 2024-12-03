from django.contrib import admin
from django.urls import path, include
from restaurant import views as reservation_views

urlpatterns = [
    path('', reservation_views.home, name='home'), 
    path('admin/', admin.site.urls),
    ## path('accounts/', include('django.contrib.auth.urls')),  
    path('', include('restaurant.urls', namespace='restaurant')), 
    path('accounts/', include('allauth.urls')),
]