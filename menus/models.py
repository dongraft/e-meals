"""Menus model."""

import uuid

# Django
from django.db import models
from django.utils import timezone

from emeals.settings import RESERVE_CLOSING


class Menu(models.Model):
    """Menus model."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(
        default=timezone.now,
        null=False,
        help_text='Date the menu will be available.'
    )
    name = models.TextField(
        max_length=50,
        blank=False,
        default="today's menu",
        help_text='Descriptive name.'
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
        """Return name."""
        return self.name

    def is_available_today(self):
        """Check if the menu is available today."""
        today = timezone.localtime().strftime('%Y-%m-%d')
        current_hour = timezone.localtime().strftime('%H')
        return self.date.strftime('%Y-%m-%d') == today and current_hour < RESERVE_CLOSING


class MenuDishes(models.Model):
    """Menus Dishes model."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu = models.ForeignKey('menus.Menu', on_delete=models.CASCADE)
    dish = models.ForeignKey('dishes.Dish', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('menu', 'dish'),)

    def __str__(self):
        """Return menu_id."""
        return '{} - {}: ${}'.format(
            self.menu.name,
            self.dish.description,
            self.dish.price
        )
