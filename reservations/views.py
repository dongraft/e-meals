"""Dishes views."""

from reservations.models import Reservation

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def list_view(request):
    """Get a list of reservations."""

    reservations = Reservation.objects.all()

    return render(request, 'reservations/list.html', {
        'reservations': reservations
    })