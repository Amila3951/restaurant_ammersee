from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Dish
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  # Import for registration

def home(request):
    dishes = Dish.objects.all()
    return render(request, "reservations/home.html", {"dishes": dishes})

def menu(request):
    dishes = Dish.objects.all()
    return render(request, "reservations/menu.html", {"dishes": dishes})

def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            num_people = form.cleaned_data["num_people"]

            reservation = Reservation(
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time,
                num_people=num_people,
            )

            reservation.save()

            return redirect("reservation_confirmation")  # Redirect to confirmation page
    else:
        form = ReservationForm()
    return render(request, "reservations/reservation_form.html", {"form": form})

def reservation_confirmation(request):
    return render(request, "reservations/reservation_confirmation.html")

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, "reservations/my_reservations.html", {"reservations": reservations})

@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation successfully updated!")
            return redirect("my_reservations")
    else:
        form = ReservationForm(instance=reservation)
    return render(request, "reservations/edit_reservation.html", {"form": form, "reservation": reservation})

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation successfully deleted!")
        return redirect("my_reservations")
    return render(request, "reservations/delete_reservation.html", {"reservation": reservation})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'reservations/register.html', {'form': form})