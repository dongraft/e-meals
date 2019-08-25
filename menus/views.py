"""Menus views."""

# Django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

# Models
from menus.models import Menu, MenuDishes
from dishes.models import Dish

# Forms
from .forms import MenuForm


@login_required
def list_view(request):
    """Get a list of menus."""
    menus = Menu.objects.all()
    return render(request, 'menus/list.html', context={
        'menus': menus
    })


@login_required
def create_view(request):
    """Create a new menu."""
    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            new_dish = Menu(**form.cleaned_data)
            new_dish.save()
            return HttpResponseRedirect(reverse('menus:menu_add_dishes', args=(new_dish.uuid,)))

    return render(request, 'menus/create.html', context={
        'form': form
    })


@login_required
def add_dishes_view(request, menu_id):
    """Add a new dish on menu."""
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
    now = timezone.now()
    today_menu = Menu.objects.latest('date')
    today_menu_date = today_menu.date.strftime('%m-%d-%Y')
    today_date = now.strftime('%m-%d-%Y')
    if today_menu_date != today_date:
        return HttpResponseRedirect(reverse('menus:not_available'))

    return HttpResponseRedirect(reverse('menus:menu_of_day', args=(
        today_menu.uuid,
    )))


def menu_of_day(request, menu_id):
    """List menu of day."""
    menu_dishes = MenuDishes.objects.all().filter(menu_id=menu_id)

    return render(request, 'menus/menu_of_day.html', context={
        'menu_dishes': menu_dishes
    })


def not_available_view(request):
    """Menu not available."""
    return render(request, 'menus/not_available.html')
