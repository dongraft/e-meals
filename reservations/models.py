"""Reservations model."""

import uuid

from django.db import models
from django.utils import timezone

# Utilities
from utils.models import EMealsBaseModel


class Reservation(models.Model):
    """Reservations model."""

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    menu_dish = models.ForeignKey(
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
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
        null=False,
        blank=False,
        help_text='Date time on which the object was created.'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""
        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        """Return menu_id."""
        return '{}: {}'.format(
            self.user.email,
            self.menu_dish,
        )
