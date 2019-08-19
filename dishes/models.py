"""Dishes model."""

# Django
from django.db import models


class Dishe(models.Model):
    """Dishes model."""

    description = models.TextField(
        'Dishe description',
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

    class Meta:
        """Meta option."""

        ordering = ['-id']

    def __str__(self):
        """Return description."""
        return self.description
