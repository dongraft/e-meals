"""Dishes views."""

# Models
from menus.models import MenuDishes
from reservations.models import Reservation

# Django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.utils import timezone

# Forms
from .forms import MenuFormReservation


@login_required
def list_view(request):
    """Get a list of reservations."""
    if request.user.is_staff:
        reservations = Reservation.objects.all()
    else:
        reservations = Reservation.objects.filter(user_id=request.user.id)
    return render(request, 'reservations/list.html', {
        'reservations': reservations
    })


@login_required
def reserve_view(request, menu_dish_id):
    """
    Generate a new reservation of menu.
    """
    menu_dish = MenuDishes.objects.get(pk=menu_dish_id)
    form = MenuFormReservation()
    if request.method == 'POST':
        form = MenuFormReservation(request.POST)
        if form.is_valid():
            new_reservation = Reservation(
                user=request.user,
                menu_dish=menu_dish,
                date=timezone.now(),
                observations=form.cleaned_data['observations']
            )
            new_reservation.save()
            return HttpResponseRedirect(reverse('reservations:menu_list'))

    return render(request, 'reservations/user/confirm_reservation.html', context={
        'menu_dish': menu_dish,
        'form': form
    })
