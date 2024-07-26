from .views import APIHPBXServers
from django.urls import path

api_hpbx_servers_view = APIHPBXServers.as_view({"get": "list",
                                                "post": "create"})

api_hpbx_server_view = APIHPBXServers.as_view({"get": "retrieve",
                                               "delete": "destroy",
                                               "post": "update"})

urlpatterns = [
    path('api/hpbx-servers', api_hpbx_servers_view, name="api_hpbx_servers_view"),
    path('api/hpbx-servers/<str:pk>', api_hpbx_server_view, name="api_hpbx_server_view"),
]
