from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Dish
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import ensure_csrf_cookie


def home(request):
    dishes = Dish.objects.all()
    return render(request, "reservations/home.html", {"dishes": dishes})


def menu(request):
    dishes = Dish.objects.all()
    return render(request, "reservations/menu.html", {"dishes": dishes})


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            return redirect('restaurant:reservation_confirmation')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})


def reservation_confirmation(request):
    return render(request, "reservations/reservation_confirmation.html")


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    context = {'reservations': reservations}
    return render(request, 'reservations/my_reservations.html', context)


@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation successfully updated!")
            return redirect("restaurant:my_reservations")
    else:
        form = ReservationForm(instance=reservation)
    return render(
        request,
        "reservations/edit_reservation.html",
        {"form": form, "reservation": reservation},
    )


@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation successfully deleted!")
        return redirect("restaurant:my_reservations")
    return render(
        request, "reservations/delete_reservation.html", {"reservation": reservation}
          )
        


@ensure_csrf_cookie
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            print(f"User {username} created successfully!")
            return redirect("restaurant:login")
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})