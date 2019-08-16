"""User admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import (
    Role,
    User
)

admin.site.register(User, UserAdmin)
admin.site.register(Role)
