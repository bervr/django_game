from .views import main, update_server
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import gameapp.urls as urls

from . import settings

app_name = 'gameapp'

urlpatterns = [
    path('', main, name='index'),
    path('admin/', admin.site.urls),
    path('update_server/', update_server, name='update_server'),
    # path('products/', include(urls, namespace='products')),
    # path('auth/', include('gameapp.urls', namespace='game_on')),
#     path('basket/', include('basketapp.urls', namespace='basket')),
#     path('admin_staff/', include('adminapp.urls', namespace='admin_staff')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)