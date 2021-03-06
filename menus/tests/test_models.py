"""Menus tests model."""

# Django
from django.test import TestCase
from django.utils import timezone

# Model
from dishes.models import Dish
from menus.models import Menu, MenuDishes


class CreateMenuTestCase(TestCase):
    """Menu test model."""

    def setUp(self):
        self.my_menu = {
            'date': '2019-08-26',
            'name': 'Monday Menu'
        }
        self.my_menu_local = {
            'date': timezone.localtime(),
            'name': 'Current Menu'
        }

    def test_create_menu(self):
        """Verify that the dish was created correctly."""
        menu = Menu.objects.create(**self.my_menu)
        self.assertIsNotNone(menu.uuid)

    def test_availability_today_menu(self):
        """
        Proof that a menu of the day is available or not
        if the time of day is less than 11 am (am).
        """
        menu = Menu.objects.create(**self.my_menu_local)
        if menu.is_available_today():
            self.assertTrue(menu.is_available_today())
        else:
            self.assertFalse(menu.is_available_today())


class CreateMenuDisheTestCase(TestCase):
    """Menu Dish test model."""

    def setUp(self):
        self.my_dish = {
            'description': 'Chicken with rice, salad, fruit',
            'price': 2990
        }
        self.my_menu = {
            'date': '2019-08-26',
            'name': 'Monday Menu'
        }

    def test_create_menu_dish(self):
        """Verify that the menu_dish was created correctly."""

        dish = Dish.objects.create(**self.my_dish)
        menu = Menu.objects.create(**self.my_menu)
        menu_dish = MenuDishes.objects.create(
            menu=menu,
            dish=dish
        )
        self.assertIsNotNone(menu_dish.uuid)
