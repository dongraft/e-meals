"""Reservation forms."""

# Django
from django import forms


class MenuFormReservation(forms.Form):
    """
    Model form for validation at the time
    the user makes a reservation
    """
    observations = forms.CharField(
        label='Observations:',
        max_length=150,
        required=True
    )
