"""Menus views."""

# Django
from django.contrib import messages
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

# Celery
from emeals.celery import send_menus


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
            menu = Menu(**form.cleaned_data)
            menu.save()

            return HttpResponseRedirect(reverse('menus:menu_edit_dishes', args=(
                menu.uuid,
            )))

    return render(request, 'menus/create.html', context={
        'form': form
    })


@login_required
def add_dishes_view(request, menu_id, dish_id):
    """
    It allows us to add the different dishes that make up the menu.
    """
    menu = Menu.objects.get(pk=menu_id)
    dish = Dish.objects.get(pk=dish_id)

    menu_dishes_taken = MenuDishes.objects.filter(
        menu_id=menu.uuid,
        dish_id=dish.uuid
    ).exists()

    if not menu_dishes_taken:
        menu_dishes = MenuDishes(menu=menu, dish=dish)
        menu_dishes.save()

    return HttpResponseRedirect(reverse('menus:menu_edit_dishes', args=(
        menu.uuid,
    )))


@login_required
def edit_dishes_view(request, menu_id):
    """
    Allows us to edit the different dishes that make up the menu.
    """
    menu = Menu.objects.get(pk=menu_id)
    my_menu_dishes = MenuDishes.objects.filter(menu_id=menu_id)
    ids_dishes_list = []
    for my_md in my_menu_dishes:
        ids_dishes_list.append(my_md.dish.uuid)

    dishes = Dish.objects.all()

    return render(request, 'menus/edit_dishes.html', context={
        'menu': menu,
        'dishes': dishes,
        'my_menu_dishes': my_menu_dishes,
        'ids_dishes_list': ids_dishes_list
    })


@login_required
def remove_dishes_view(request, menu_id, menu_dish_id):
    """
    It allows us to remove a dish from a respective menu,
    as long as the menu has not been confirmed.
    """
    menu = Menu.objects.get(pk=menu_id)
    menu_dish = MenuDishes.objects.get(pk=menu_dish_id)

    if menu.is_confirmed:
        msg = 'We are sorry, but this menu: {} has already been confirmed, '
        msg += 'therefore you can no longer edit your dishes.'.format(menu.name)
        messages.info(request, msg)
    else:
        menu_dish.delete()

    return HttpResponseRedirect(reverse('menus:menu_edit_dishes', args=(
        menu.uuid,
    )))


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


@login_required
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
            return HttpResponseRedirect(reverse('menus:menu_edit_dishes', args=(
                menu.uuid,
            )))

        menu.is_confirmed = True
        menu.save()

    return HttpResponseRedirect(reverse('menus:menu_list'))


@login_required
def menu_notify(request, menu_id):
    """
    Notify menu

    View that allows you to manually notify the menu of the day
    in case it is necessary to do it in addition to the periodic task.
    """
    try:
        menu = Menu.objects.get(pk=menu_id)
        if menu.is_available_today:
            send_menus.delay()
            msg = 'A notification will be sent to the slack channel for the {} menu'.format(menu.name)
            messages.info(
                request,
                msg
            )
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('not_found'))

    return HttpResponseRedirect(reverse('menus:menu_list'))
