"""Reservations tests model."""

# Django
from django.test import TestCase
from django.utils import timezone

# Models
from dishes.models import Dish
from menus.models import Menu, MenuDishes
from reservations.models import Reservation
from users.models import User


class CreateReservationTestCase(TestCase):
    """Reservation test model."""

    def setUp(self):
        self.user = User.objects.create(email='alanbrito@gmail.com', password='1p2o3i4u5yha')
        self.dish = Dish.objects.create(description="Dish Name", price=2990)
        self.menu = Menu.objects.create(date=timezone.localtime(), name='Current Menu')
        self.menu_dish = MenuDishes.objects.create(menu=self.menu, dish=self.dish)

    def test_create_reservation(self):
        """Verify that the reservation was created correctly."""
        reservation = Reservation.objects.create(
            user=self.user,
            menu_dish=self.menu_dish,
            date=timezone.localtime(),
            observations="Observations to my food"
        )
        self.assertIsNotNone(reservation.uuid)
