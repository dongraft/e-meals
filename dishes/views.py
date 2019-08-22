"""Dishes views."""

from dishes.models import Dish

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import DisheForm


@login_required
def list_view(request):
    """Get a list of dishes."""

    dishes = Dish.objects.all()

    return render(request, 'dishes/list.html', {
        'dishes': dishes
    })


@login_required
def create_view(request):
    """Create a new dishe."""

    form = DisheForm()

    if request.method == 'POST':
        form = DisheForm(request.POST)
        if form.is_valid():
            new_dish = Dish(**form.cleaned_data)
            new_dish.save()

            return HttpResponseRedirect(reverse('dishes:dish_list'))

    return render(request, 'dishes/create.html', context={
        'form': form
    })
