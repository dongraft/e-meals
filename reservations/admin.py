"""Reservations admin classes."""

# Django
from django.contrib import admin

# Models
from reservations.models import Reservation

admin.site.register(Reservation)
