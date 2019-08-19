"""Menus URLs."""

# Django
from django.urls import path

# View
from menus import views as menu_views

urlpatterns = [
    path(
        route='',
        view=menu_views.list_view,
        name='menu_list'
    ),
    path(
        route='create/',
        view=menu_views.create_view,
        name='menu_create'
    ),
    path(
        route='<int:menu_id>/dishes/add/',
        view=menu_views.add_dishes_view,
        name='menu_add_dishes'
    )
]
