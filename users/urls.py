"""Users URLs."""

# Django
from django.urls import path

# View
from users import views as users_views

urlpatterns = [
    # Management
    path(
        route='login/',
        view=users_views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=users_views.logout_view,
        name='logout'
    ),
]
