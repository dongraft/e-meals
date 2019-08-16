"""Dishes views."""

from dishes.models import Dishe

from django.shortcuts import render


def list_view(request):
    """Get a list of dishes."""

    dishes = Dishe.objects.all()

    return render(request, 'dishes/list.html', {
        'dishes': dishes
    })
