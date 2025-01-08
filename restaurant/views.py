from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Dish
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
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User



def home(request):
    """
    View for the home page.
    Handles redirecting users based on authentication status and displays a list of dishes.
    """
    if request.method == "POST":
        if request.user.is_authenticated:
            return redirect(
                "restaurant:make_reservation"
            )  # Redirect to make a reservation if logged in
        else:
            return redirect("account_login")  # Redirect to login if not logged in
    else:
        dishes = Dish.objects.all()  # Retrieve all dishes from the database
        return render(
            request, "reservations/home.html", {"dishes": dishes}
        )  # Render the home page with dishes


def menu(request):
    """
    View for the menu page.
    Displays a list of dishes.
    """
    dishes = Dish.objects.all()  # Retrieve all dishes from the database
    context = {"dishes": dishes}
    return render(
        request, "reservations/menu.html", context
    )  # Render the menu page with dishes


def make_reservation(request):
    """
    View for making a reservation.
    Handles form submission, checks availability, and saves the reservation.
    """
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            num_people = form.cleaned_data["num_people"]

            # Check availability

            reservations_at_that_time = Reservation.objects.filter(
                date=date, time=time
            )  # Get reservations for the specified date and time
            total_people_at_that_time = (
                reservations_at_that_time.aggregate(Sum("num_people"))[
                    "num_people__sum"
                ]
                or 0
            )  # Calculate the total number of people with reservations at that time

            if (
                total_people_at_that_time + num_people > settings.RESTAURANT_CAPACITY
            ):  # Check if there is enough space
                # If there is not enough space, display an error message

                form.add_error(None, "Sorry, we don't have enough space at that time.")
            else:
                # If there is enough space, try to save the reservation

                try:
                    reservation = form.save(
                        commit=False
                    )  # Create the Reservation object but don't save yet
                    if request.user.is_authenticated:
                        reservation.user = (
                            request.user
                        )  # Associate the reservation with the logged-in user
                    reservation.save()  # Save the reservation to the database (this will call the clean() method)

                    # Redirect to confirmation page after successful reservation

                    return redirect(
                        "restaurant:reservation_confirmation",
                        reservation_id=reservation.id,
                    )
                except ValidationError as e:
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

    template_name = "account/login.html"  # Specify the custom template


@login_required  # Requires user to be logged in
def my_reservations(request):
    """
    View for displaying a user's reservations.
    Requires user to be logged in.
    """
    reservations = Reservation.objects.filter(user=request.user).order_by(
        "date", "time"
    )  # Fetch reservations for the logged-in user and order them
    context = {
        "reservations": reservations
    }  # Create a context dictionary to pass to the template
    return render(
        request, "reservations/my_reservations.html", context
    )  # Render the template with the context


@login_required
def edit_reservation(request, reservation_id):
    """
    View for editing a reservation.
    Requires user to be logged in and the reservation to belong to the user.
    """
    # Retrieve the reservation object, ensuring it exists and belongs to the logged-in user.

    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
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
        )  # Populate form with existing reservation data
    return render(
        request,
        "reservations/edit_reservation.html",
        {
            "form": form,
            "reservation": reservation,
        },  # Pass form and reservation to the template
    )


@login_required
def delete_reservation(request, reservation_id):
    """
    View for deleting a reservation.
    Requires user to be logged in and the reservation to belong to the user.
    """
    # Retrieve the reservation object, ensuring it exists and belongs to the logged-in user.

    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)

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
        request,
        "reservations/delete_reservation.html",
        {
            "reservation": reservation
        },  # Pass reservation to the template for confirmation
    )


@ensure_csrf_cookie
def register(request):
    """
    View for user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('restaurant:home')  # Redirect to home page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})



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
    )


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_reservations(request):
    reservations = Reservation.objects.all()
    context = {"reservations": reservations}
    return render(request, "reservations/admin_reservations.html", context)


def add_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                reservation = form.save(commit=False) 
                reservation.user = user
                reservation.save()

                return redirect('restaurant:admin_reservations')
            else:
               
                form.add_error('email', 'User with this email address does not exist.')
    else:
        form = ReservationForm()
    return render(request, 'reservations/add_reservation.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
        return redirect("restaurant:admin_reservations")
    return render(
        request,
        "reservations/admin_delete_reservation.html",
        {"reservation": reservation},
    )


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("restaurant:admin_reservations")
    else:
        form = ReservationForm(instance=reservation)
    return render(
        request,
        "reservations/admin_edit_reservation.html",
        {"form": form, "reservation": reservation},
    )