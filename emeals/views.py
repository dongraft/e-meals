"""Menus views."""

# Django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Models
from menus.models import Menu, MenuDishes


def home_view(request):
    """Display welcome view."""
    return render(request, 'emeals/home.html')