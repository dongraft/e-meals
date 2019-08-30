"""Menus views."""

# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def home_view(request):
    """
    Display welcome view
    When the user is logged in and accesses the initial route,
    he is redirected to the reservation list.
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('reservations:menu_list'))

    return render(request, 'emeals/home.html')


def not_found_view(request):
    """Page not found view."""
    return render(request, 'emeals/errors/404.html')


def server_error_view(request):
    """Internal server error view."""
    return render(request, 'emeals/errors/500.html')
