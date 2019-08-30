"""Menu forms."""

from datetime import datetime

# Django
from django import forms
from django.utils import timezone

# Models
from menus.models import Menu


class MenuForm(forms.Form):
    """Menu Form."""

    date = forms.DateField(
        label='Date of Menu:',
        initial=datetime.today,
        required=True
    )
    name = forms.CharField(
        label='Monday day menu!',
        max_length=150,
        min_length=4,
        required=True
    )

    def clean_date(self):
        """
        Model validations by date field

        A menu cannot be added under a date that is already registered for
        another, and menus cannot be added for dates before the current day.
        """
        creation_date = self.cleaned_data['date']
        menu_taken = Menu.objects.filter(date=creation_date).exists()
        today = timezone.localtime().strftime('%Y-%m-%d')
        if menu_taken:
            raise forms.ValidationError('A menu for the selected date already exists, please select a new one.')
        if creation_date.strftime('%Y-%m-%d') < today:
            raise forms.ValidationError('You cannot select a date before today.')

        return creation_date
