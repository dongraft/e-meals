"""Menus model."""

from django.db import models


class Menu(models.Model):
    """Menus model."""

    date = models.DateField(null=False)
    name = models.TextField(
        max_length=50,
        blank=False,
        default="today's menu"
    )

    def __str__(self):
        """Return name."""
        return self.name


class MenuDishes(models.Model):
    """Menus Dishes model."""

    menu = models.ForeignKey('menus.Menu', on_delete=models.CASCADE)
    dishe = models.ForeignKey('dishes.Dishe', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('menu', 'dishe'),)

    def __str__(self):
        """Return menu_id."""
        return '{} - {}: ${}'.format(
            self.menu.name,
            self.dishe.description,
            self.dishe.price
        )
