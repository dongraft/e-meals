"""emeals URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include,
    path
)

urlpatterns = [
    # Dont forget, delete at the end
    path('admin/', admin.site.urls),

    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('dishes/', include(('dishes.urls', 'dishes'), namespace='dishes')),

    path('menus/', include(('menus.urls', 'menus'), namespace='menus')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
