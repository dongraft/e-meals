"""Menus views."""

# Django
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Models
from menus.models import Menu, MenuDishes
from dishes.models import Dish

# Forms
from .forms import MenuForm


@login_required
def list_view(request):
    """
    Get a list of all registered menus.
    """
    menus = Menu.objects.all()
    return render(request, 'menus/list.html', context={
        'menus': menus
    })


@login_required
def create_view(request):
    """
    Create a new menu

    A new menu will be generated given a particular date, if for the selected
    date a menu already exists, it will be canceled and the user will be notified
    that he cannot add another menu for the same date.
    """
    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            new_dish = Menu(**form.cleaned_data)
            new_dish.save()
            return HttpResponseRedirect(reverse(
                'menus:menu_add_dishes',
                args=(new_dish.uuid,)
            ))

    return render(request, 'menus/create.html', context={
        'form': form
    })


@login_required
def add_dishes_view(request, menu_id):
    """
    It allows us to add the different dishes that make up the menu.
    """
    menu = Menu.objects.get(pk=menu_id)
    dishes = Dish.objects.all()

    if request.method == 'POST':
        dishes_list = request.POST.getlist('dishes_list')
        for dish_id in dishes_list:
            dish = Dish.objects.get(pk=dish_id)
            menu_dishes = MenuDishes(menu=menu, dish=dish)
            menu_dishes.save()
        return HttpResponseRedirect(reverse('menus:menu_list'))

    return render(request, 'menus/add_dishes.html', context={
        'menu': menu,
        'dishes': dishes
    })


def check_menu_of_day(request):
    """
    Method that is responsible for verifying if there is
    a menu available to be offered to users
    """
    try:
        menu = Menu.objects.latest('date')
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('not_found'))

    if not menu.is_available_today:
        return HttpResponseRedirect(reverse('menus:not_available'))

    return HttpResponseRedirect(reverse('menus:menu_of_day', args=(
        menu.uuid,
    )))


def menu_of_day(request, menu_id):
    """List menu of day."""
    try:
        menu = Menu.objects.get(pk=menu_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('not_found'))

    if menu.is_available_today:
        menu_dishes = MenuDishes.objects.all().filter(menu_id=menu_id)
        return render(request, 'menus/menu_of_day.html', context={
            'menu_dishes': menu_dishes
        })

    return HttpResponseRedirect(reverse('menus:not_available'))


def not_available_view(request):
    """Menu not available."""
    return render(request, 'menus/not_available.html')


def confirm_view(request, menu_id):
    """
    Confirm menu status

    The menu will be available as long as it is confirmed by the admin / seller / Nora user,
    once confirmed it can no longer be modified
    """
    try:
        menu = Menu.objects.get(pk=menu_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('not_found'))

    if not menu.is_confirmed:
        menu_dishes_taken = MenuDishes.objects.filter(menu_id=menu.uuid).exists()
        if not menu_dishes_taken:
            return HttpResponseRedirect(reverse('menus:menu_add_dishes', args=(
                menu.uuid,
            )))

        menu.is_confirmed = True
        menu.save()

    return HttpResponseRedirect(reverse('menus:menu_list'))
