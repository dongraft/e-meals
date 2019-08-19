"""Menu forms."""

import datetime

# Django
from django import forms


class MenuForm(forms.Form):
    """Menu Form."""

    date = forms.DateField(
        label='Date of Menu:',
        initial=datetime.date.today,
        required=True
    )
    name = forms.CharField(
        label='Monday day menu!',
        max_length=150,
        min_length=4,
        required=True
    )
