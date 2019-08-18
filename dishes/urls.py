"""Dishes URLs."""

# View
from dishes import views as dishes_views

# Django
from django.urls import path

urlpatterns = [
    path(
        route='list/',
        view=dishes_views.list_view,
        name='dishe_list'
    ),
    path(
        route='create/',
        view=dishes_views.create_view,
        name='dishe_create'
    ),
]
