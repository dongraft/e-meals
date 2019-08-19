"""Menus views."""

# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Models
from menus.models import Menu, MenuDishes
from dishes.models import Dishe

# Forms
from .forms import MenuForm


def list_view(request):
    """Get a list of menus."""

    menus = Menu.objects.all()

    return render(request, 'menus/list.html', context={
        'menus': menus
    })


def create_view(request):
    """Create a new menu."""

    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            new_dishe = Menu(**form.cleaned_data)
            new_dishe.save()
            return HttpResponseRedirect(reverse('menus:menu_add_dishes', args=(new_dishe.id,)))

    return render(request, 'menus/create.html', context={
        'form': form
    })


def add_dishes_view(request, menu_id):
    """Add a new dishe on menu."""

    menu = Menu.objects.get(pk=menu_id)
    dishes = Dishe.objects.all()

    if request.method == 'POST':
        dishes_list = request.POST.getlist('dishes_list')
        for dishe_id in dishes_list:
            dishe = Dishe.objects.get(pk=dishe_id)
            menu_dishes = MenuDishes(menu=menu, dishe=dishe)
            menu_dishes.save()

        return HttpResponseRedirect(reverse('menus:menu_list'))

    return render(request, 'menus/add_dishes.html', context={
        'menu': menu,
        'dishes': dishes
    })
