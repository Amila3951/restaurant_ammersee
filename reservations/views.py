from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Dish
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    dishes = Dish.objects.all()
    return render(request, 'reservations/home.html', {'dishes': dishes})

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'reservations/menu.html', {'dishes': dishes})

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            messages.success(request, 'Rezervacija uspješno kreirana!')
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_success(request):
    return render(request, 'reservations/reservation_success.html')

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})

@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rezervacija uspješno ažurirana!')
            return redirect('my_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/edit_reservation.html', {'form': form, 'reservation': reservation})

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Rezervacija uspješno izbrisana!')
        return redirect('my_reservations')
    return render(request, 'reservations/delete_reservation.html', {'reservation': reservation})