from django.urls import path, include
from restaurant import views as reservation_views
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path("", reservation_views.home, name="home"),
    path(
        "restaurant/", include("restaurant.urls", namespace="restaurant")
    ),
    path("admin/", admin.site.urls),
    path("", include("restaurant.urls")),
    path(
        "my_reservations/",
        include("restaurant.urls", namespace="reservations"),
    ),
    path("", include("restaurant.urls", namespace="restaurant")),
    path("accounts/", include("allauth.urls")),
    path(
        "menu/",
        TemplateView.as_view(template_name="reservations/menu.html"),
        name="menu",
    ),
]
