from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.views import LoginView
from django.db.models import Sum
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import Http404


def home(request):
    """
    View for the home page.
    Handles redirecting users based on authentication status.
    """
    if request.method == "POST":
        if request.user.is_authenticated:  # Check if the user is logged in
            return redirect("restaurant:make_reservation")  # Redirect to make a reservation if logged in  # noqa
        else:
            return redirect("account_login")  # Redirect to login if not logged in  # noqa
    else:
        return render(request, "reservations/home.html")


def menu(request):
    """
    View for the menu page.
    """
    return render(request, "reservations/menu.html")


def make_reservation(request):
    """
    View for making a reservation.
    Handles form submission, checks availability, and saves the reservation.
    """
    if request.method == "POST":
        form = ReservationForm(
            request.POST
        )
        if form.is_valid():  # Check if the form is valid
            date = form.cleaned_data["date"]  # Get the reservation date
            time = form.cleaned_data["time"]  # Get the reservation time
            num_people = form.cleaned_data["num_people"]  # Get the number of people  # noqa

            # Check availability

            reservations_at_that_time = Reservation.objects.filter(
                date=date, time=time
            )  # Get reservations for the specified date and time
            total_people_at_that_time = (
                reservations_at_that_time.aggregate(Sum("num_people"))[
                    "num_people__sum"
                ]
                or 0
            )  # Calculate the total number of people with reservations at that time  # noqa

            if (
                total_people_at_that_time + num_people > settings.RESTAURANT_CAPACITY  # noqa
            ):  # Check if there is enough space
                # If there is not enough space, display an error message

                form.add_error(None, "Sorry, we don't have enough space at that time.")  # noqa
            else:
                # If there is enough space, try to save the reservation

                try:
                    reservation = form.save(
                        commit=False
                    )  # Create the Reservation object but don't save yet
                    if request.user.is_authenticated:  # Check if the user is logged in  # noqa
                        reservation.user = (
                            request.user
                        )  # Associate the reservation with the logged-in user
                    reservation.save()  # Save the reservation to the database

                    # Redirect to confirmation page after successful reservation  # noqa

                    return redirect(
                        "restaurant:reservation_confirmation",
                        reservation_id=reservation.id,
                    )
                except ValidationError as e:  # Catch validation errors
                    form.add_error(None, e)  # Add the error to the form
    else:
        form = ReservationForm()  # Create an empty reservation form
    return render(
        request, "reservations/make_reservation.html", {"form": form}
    )  # Render the make reservation page with the form


class MyLoginView(LoginView):
    """
    Custom login view to use a custom template.
    """
    template_name = "account/login.html"


@login_required  # Requires user to be logged in
def my_reservations(request):
    """
    View for displaying a user's reservations.
    """
    reservations = Reservation.objects.filter(user=request.user).order_by(
        "date", "time"
    )  # Fetch reservations for the logged-in user and order them
    context = {
        "reservations": reservations
    }
    return render(
        request, "reservations/my_reservations.html", context
    )  # Render the template with the context


@login_required  # Requires user to be logged in
def edit_reservation(request, reservation_id):
    """
    View for editing a reservation.
    """
    # Retrieve the reservation object, ensuring it exists and belongs to the logged-in user.  # noqa

    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)  # noqa

    if request.method == "POST":
        form = ReservationForm(
            request.POST, instance=reservation
        )
        if form.is_valid():  # Validate the form data
            form.save()  # Save the updated reservation
            messages.success(
                request, "Reservation successfully updated!"
            )  # Display success message
            return redirect(
                "restaurant:my_reservations"
            )  # Redirect to user's reservations page
    else:
        form = ReservationForm(
            instance=reservation
        )
    return render(
        request,
        "reservations/edit_reservation.html",
        {"form": form, "reservation": reservation},
    )  # Pass form and reservation to the template


@login_required  # Requires user to be logged in
def delete_reservation(request, reservation_id):
    """
    View for deleting a reservation.
    """
    # Retrieve the reservation object, ensuring it exists and belongs to the logged-in user.  # noqa

    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)  # noqa

    if (
        request.method == "POST"
    ):  # Check if the request is a POST (confirmation of deletion)
        reservation.delete()  # Delete the reservation
        messages.success(
            request, "Reservation successfully deleted!"
        )  # Display success message
        return redirect(
            "restaurant:my_reservations"
        )  # Redirect to user's reservations page
    return render(
        request, "reservations/delete_reservation.html", {"reservation": reservation}  # noqa
    )  # Pass reservation to the template for confirmation


@ensure_csrf_cookie  # Ensures that the CSRF cookie is set for the response
def register(request):
    """
    View for user registration.
    """
    if request.method == "POST":
        form = UserCreationForm(
            request.POST
        )
        if form.is_valid():  # Check if the form is valid
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user
            request.session["registration_successful"] = (
                True
            )
            return redirect(
                "restaurant:home"
            )  # Redirect to home page after registration
    else:
        form = CustomUserCreationForm()  # Create an empty CustomUserCreationForm # noqa
    return render(
        request, "account/signup.html", {"form": form}
    )  # Render the signup page with the form


def reservation_confirmation(request, reservation_id):
    """
    View for displaying the reservation confirmation page.
    """
    reservation = get_object_or_404(
        Reservation, pk=reservation_id
    )  # Retrieve the reservation or return 404
    return render(
        request,
        "reservations/reservation_confirmation.html",
        {"reservation": reservation},
    )  # Render the confirmation page with the reservation


@login_required  # Requires user to be logged in
@user_passes_test(lambda u: u.is_superuser)  # Requires user to be a superuser
def admin_reservations(request):
    """
    View for displaying all reservations to admin users.
    """
    reservations = Reservation.objects.all()  # Retrieve all reservations
    context = {
        "reservations": reservations
    }  # Create a context dictionary to pass to the template
    return render(
        request, "reservations/admin_reservations.html", context
    )  # Render the admin reservations page with the context


@login_required  # Requires user to be logged in
@user_passes_test(lambda u: u.is_superuser)  # Requires user to be a superuser
def add_reservation(request):
    """
    View for adding a reservation (admin view).
    Allows adding reservations with any email address,
    without checking for user registration.
    """
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            # Directly save the reservation without checking for user
            reservation.save()
            return redirect("restaurant:admin_reservations")
    else:
        form = ReservationForm()
    return render(request, "reservations/add_reservation.html", {"form": form})


@login_required  # Requires user to be logged in
@user_passes_test(lambda u: u.is_superuser)  # Requires user to be a superuser
def admin_delete_reservation(request, pk):
    """
    View for deleting a reservation (admin view).
    """
    reservation = get_object_or_404(
        Reservation, pk=pk
    )  # Retrieve the reservation or return 404
    if (
        request.method == "POST"
    ):
        reservation.delete()  # Delete the reservation
        return redirect(
            "restaurant:admin_reservations"
        )  # Redirect to the admin reservations page
    return render(
        request,
        "reservations/admin_delete_reservation.html",
        {"reservation": reservation},
    )  # Render the delete confirmation page with the reservation


@login_required  # Requires user to be logged in
@user_passes_test(lambda u: u.is_superuser)  # Requires user to be a superuser
def admin_edit_reservation(request, pk):
    """
    View for editing a reservation (admin view).
    """
    reservation = get_object_or_404(
        Reservation, pk=pk
    )
    if request.method == "POST":
        form = ReservationForm(
            request.POST, instance=reservation
        )
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the updated reservation
            return redirect(
                "restaurant:admin_reservations"
            )  # Redirect to the admin reservations page
    else:
        form = ReservationForm(
            instance=reservation
        )  # Populate form with existing reservation data
    return render(
        request,
        "reservations/admin_edit_reservation.html",
        {"form": form, "reservation": reservation},
    )  # Render the edit reservation page with the form and reservation
