"""Dishes views."""

from dishes.models import Dishe

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import DisheForm


def list_view(request):
    """Get a list of dishes."""

    dishes = Dishe.objects.all()

    return render(request, 'dishes/list.html', {
        'dishes': dishes
    })


def create_view(request):
    """Create a new dishe."""

    form = DisheForm()

    if request.method == 'POST':
        form = DisheForm(request.POST)
        if form.is_valid():
            new_dishe = Dishe(**form.cleaned_data)
            new_dishe.save()

            return HttpResponseRedirect(reverse('dishes:list'))

    return render(request, 'dishes/create.html', context={
        'form': form
    })
