"""Reservations URLs."""

# Django
from django.urls import path

# View
from reservations import views as reservation_views

urlpatterns = [
    path(
        route='',
        view=reservation_views.list_view,
        name='menu_list'
    ),
    path(
        route='<uuid:menu_dish_id>/reservate',
        view=reservation_views.reserve_view,
        name='menu_reserve'
    ),
]
