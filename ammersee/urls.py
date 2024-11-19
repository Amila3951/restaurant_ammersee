from django.contrib import admin
from django.urls import path, include
from restaurant import views as reservation_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reservation_views.home, name='home'), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('restaurant/', include('restaurant.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'), 
]