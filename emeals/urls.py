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
    )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
