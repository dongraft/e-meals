"""Dish test model."""

# Django
from django.test import TestCase

# Model
from dishes.models import Dish


class CreateDishTestCase(TestCase):
    """Dish test model."""

    def setUp(self):
        self.tallarines = {
            'description': 'Porotos con rienda, ensalada de tomates, galea',
            'price': 2990
        }

    def test_create_dish(self):
        """Verify that the dish was created correctly."""
        new_dish = Dish.objects.create(**self.tallarines)
        self.assertIsNotNone(new_dish.uuid)
