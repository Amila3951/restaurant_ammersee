from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Dish
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.views import LoginView 
from django.db.models import Sum
from django.conf import settings

def home(request):
    if request.method == 'POST':  
        if request.user.is_authenticated:
            return redirect('restaurant:make_reservation')  
        else:
            return redirect('account_login')  
    else: 
        dishes = Dish.objects.all()
        return render(request, "reservations/home.html", {"dishes": dishes})

def menu(request):
    dishes = Dish.objects.all()
    context = {'dishes': dishes}
    return render(request, 'reservations/menu.html', context)


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            num_people = form.cleaned_data['num_people']

            # Check availability
            reservations_at_that_time = Reservation.objects.filter(date=date, time=time)
            total_people_at_that_time = reservations_at_that_time.aggregate(Sum('num_people'))['num_people__sum'] or 0

            if total_people_at_that_time + num_people > settings.RESTAURANT_CAPACITY:
                # If there is not enough space, display an error message
                form.add_error(None, "Sorry, we don't have enough space at that time.") 
            else:
                # If there is enough free seats, save the reservation
                print(form.cleaned_data)
                reservation = form.save(commit=False)  # Create the Reservation object but don't save yet
                if request.user.is_authenticated:
                    reservation.user = request.user
                reservation.save()  # Save the reservation to the database
                return redirect('restaurant:reservation_confirmation', reservation_id=reservation.id)
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})


class MyLoginView(LoginView):
    template_name = 'account/login.html'


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
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            print(f"User {username} created successfully!")

            login(request, user) 
            return redirect("restaurant:home") 
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})
    

def reservation_confirmation(request, reservation_id): # Corrected view
    reservation = get_object_or_404(Reservation, pk=reservation_id) 
    return render(request, "reservations/reservation_confirmation.html", {'reservation': reservation})