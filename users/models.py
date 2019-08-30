"""User model."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User model.
    Extend from Django's Abstract User,
    change the username field to email.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )

    def __str__(self):
        """Return email."""
        return self.email
