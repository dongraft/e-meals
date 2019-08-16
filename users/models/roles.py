"""Roles model."""

# Django
from django.db import models


class Role(models.Model):
    """Roles model."""

    name = models.CharField(
        'Role name',
        max_length=30,
        null=False
    )

    def __str__(self):
        """Return role name."""
        return self.name
