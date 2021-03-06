"""Dishes URLs."""

# View
from dishes import views as dishes_views

# Django
from django.urls import path

urlpatterns = [
    path(
        route='',
        view=dishes_views.list_view,
        name='dish_list'
    ),
    path(
        route='create/',
        view=dishes_views.create_view,
        name='dish_create'
    ),
]
