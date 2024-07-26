from django.contrib import admin
from django.urls import path, include
from .views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('servers.urls')),
    path('', include('carrier_monitoring.urls')),
    path('', home_view)
]
