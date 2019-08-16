"""Menus admin classes."""

# Django
from django.contrib import admin

# Models
from menus.models import Menu, MenuDishes

admin.site.register(Menu)
admin.site.register(MenuDishes)
