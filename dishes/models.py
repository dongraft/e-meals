"""Dishes model."""

import uuid

# Django
from django.db import models
from django.utils import timezone

class Dish(models.Model):
    """Dishes model."""

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(
        'Dish description__',
        null=False,
        help_text='Description of the elements that will be part of the dish'
    )
    price = models.PositiveIntegerField(default=0)
    is_enabled = models.BooleanField(
        'is enabled',
        default=True,
        help_text=(
            'Help to distinguish the dishes that are enabled from those that are not'
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
        """Return description."""
        return self.description

