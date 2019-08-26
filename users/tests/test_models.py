"""Users test model."""

# Django
from django.db.utils import IntegrityError
from django.test import TestCase

# Model
from users.models import User


class CreateUserTestCase(TestCase):
    """
    Evaluate that the User model allows us to
    create a user correctly.
    """

    def setUp(self):
        self.alan = {
            'email': 'alanbrito@gmail.com',
            'password': '4D186321C1A7',
            'first_name': 'Alan',
            'last_name': 'Brito'
        }
        self.alonso = {
            'email': 'alanbrito@gmail.com',
            'password': 'A1821C16374D',
            'first_name': 'Alonso',
            'last_name': 'Brito'
        }

    def test_create_user(self):
        """Verify that the user was created correctly."""
        user_alan = User.objects.create(**self.alan)
        self.assertIsNotNone(user_alan.id)

    def test_unique_user_creation(self):
        """Proof that you cannot create a user with the same."""
        User.objects.create(**self.alan)
        with self.assertRaises(Exception) as raised:
            User.objects.create(**self.alonso)
        # Raise exception duplicate key value violates unique constraint
        self.assertEqual(IntegrityError, type(raised.exception))
