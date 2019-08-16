"""Reservations model."""

from django.db import models


class Reservation(models.Model):
    """Reservations model."""

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    menu_dishe = models.ForeignKey(
        'menus.MenuDishes',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=False,
        blank=False,
        help_text='Date time on which the reservation was created.'
    )
    observations = models.TextField(
        'Employees Observations',
        null=False,
        help_text='Customizations of my dishes'
    )
    is_confirmed = models.BooleanField(
        'confirmed by seller/Nora',
        default=False,
        help_text=(
            'Help easily distinguish status of Reservation.'
        )
    )

    def __str__(self):
        """Return menu_id."""
        return '{}: {}'.format(
            self.user.email,
            self.menu_dishe,
        )
