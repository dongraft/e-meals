"""emeals URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include,
    path
)

# View
from emeals import views as emeals_views

urlpatterns = [
    # Dont forget, delete at the end
    path('admin/', admin.site.urls),

    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('dishes/', include(('dishes.urls', 'dishes'), namespace='dishes')),

    path('menus/', include(('menus.urls', 'menus'), namespace='menus')),

    path('reservations/', include(('reservations.urls', 'reservations'), namespace='reservations')),

    path(
      route='',
      view=emeals_views.home_view,
      name='emeals_home'
    ),
    path(
      route='404',
      view=emeals_views.not_found_view,
      name='not_found'
    ),
    path(
      route='500',
      view=emeals_views.server_error_view,
      name='server_error'
    )

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
