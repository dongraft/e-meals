"""Dishe forms."""

# Models
# from dishes.models import Dishe

# Django
from django import forms


class DisheForm(forms.Form):
    """Dishe Form."""

    description = forms.CharField(
        label='Dishe description:',
        max_length=150,
        required=True
    )
    price = forms.IntegerField(
        label='Enter price',
        min_value=1,
        max_value=1000000,
        required=True
    )
