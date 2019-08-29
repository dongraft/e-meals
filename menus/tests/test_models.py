"""Menu test model."""

# Django
from django.test import TestCase
from django.utils import timezone

# Model
from menus.models import Menu


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

    def test_create_dish(self):
        """Verify that the dish was created correctly."""
        menu = Menu.objects.create(**self.my_menu)
        self.assertIsNotNone(menu.uuid)

    def test_availability_today_menu(self):
        """
        Proof that a menu of the day is available or not
        if the time of day is less than 11 am (am).
        """
        menu = Menu.objects.create(**self.my_menu_local)
        now = timezone.localtime()
        current_time = now.strftime('%H')
        if current_time < '11':
            self.assertTrue(menu.is_available_today())
        else:
            self.assertFalse(menu.is_available_today())
