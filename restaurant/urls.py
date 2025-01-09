from . import views as reservation_views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import MyLoginView

app_name = "restaurant"  # Namespace for the app

urlpatterns = [
    path("", views.home, name="home"),  # Home page
    path("menu/", views.menu, name="menu"),  # Menu page
    path(
        "make/", views.make_reservation, name="make_reservation"
    ),  # Make a reservation page
    path(
        "my_reservations/", views.my_reservations, name="my_reservations"
    ),  # My reservations page
    path(
        "my_reservations/<int:reservation_id>/edit/",  # Edit reservation page
        views.edit_reservation,
        name="edit_reservation",
    ),
    path(
        "my_reservations/<int:reservation_id>/delete/",  # Delete reservation page  # noqa
        views.delete_reservation,
        name="delete_reservation",
    ),
    path(
        "accounts/login/", MyLoginView.as_view(), name="account_login"
    ),  # Login page
    path(
        "accounts/logout/",  # Logout page
        auth_views.LogoutView.as_view(
            next_page="restaurant:home"
        ),  # Redirect to home after logout
        name="account_logout",
    ),
    path(
        "confirmation/<int:reservation_id>/",  # Reservation confirmation page
        views.reservation_confirmation,
        name="reservation_confirmation",
    ),
    # Admin URLs
    path(
        "admin/reservations/",
        views.admin_reservations,
        name="admin_reservations",
    ),  # Admin reservations page
    path(
        "admin/reservations/add/",
        views.add_reservation,
        name="add_reservation",
    ),  # Add reservation page (admin)
    path(
        "admin/reservations/<int:pk>/edit/",
        views.admin_edit_reservation,
        name="admin_edit_reservation",
    ),  # Edit reservation page (admin)
    path(
        "admin/reservations/<int:pk>/delete/",
        views.admin_delete_reservation,
        name="admin_delete_reservation",
    ),  # Delete reservation page (admin)
]
