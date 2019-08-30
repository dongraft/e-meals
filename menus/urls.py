"""Menus URLs."""

# Django
from django.urls import path

# View
from menus import views as menu_views

urlpatterns = [
    path(route='', view=menu_views.list_view, name='menu_list'),

    path(route='create/', view=menu_views.create_view, name='menu_create'),

    path(route='<uuid:menu_id>/confirm', view=menu_views.confirm_view, name='menu_confirm'),

    path(route='<uuid:menu_id>/notify', view=menu_views.menu_notify, name='menu_notify' ),

    path(route='check-today-menu/', view=menu_views.check_menu_of_day, name="check_menu_of_day"),

    path(route='not-available/', view=menu_views.not_available_view, name="not_available"),

    path(route='<uuid:menu_id>/dishes/edit/', view=menu_views.edit_dishes_view, name='menu_edit_dishes'),

    path(
        route='<uuid:menu_id>/dishes/<uuid:dish_id>/add/',
        view=menu_views.add_dishes_view,
        name='menu_add_dishes'
    ),

    path(
        route='<uuid:menu_id>/dishes/<uuid:menu_dish_id>/remove/',
        view=menu_views.remove_dishes_view,
        name='menu_remove_dishes'
    ),

    path(route='<uuid:menu_id>', view=menu_views.menu_of_day, name='menu_of_day')
]
