from .views import CarrierMonServerData, CarrierMonitoringView, CarrierMonUserView
from django.urls import path

carrier_mon_server_data = CarrierMonServerData.as_view({"get": "list"})

carr_mon_servers = CarrierMonitoringView.as_view({"get": "list",
                                                  "post": "create"})

carr_mon_server = CarrierMonitoringView.as_view({"get": "retrieve",
                                                 "delete": "destroy",
                                                 "post": "update",
                                                 "put": "checked"})

carr_mon_users = CarrierMonUserView.as_view({"get": "get_users",
                                             "post": "create_mon_user"})

carr_mon_user = CarrierMonUserView.as_view({"get": "retrieve",
                                            "delete": "destroy",
                                            "post": "update_mon_user"})

urlpatterns = [
    path('api/carrier-mon-server-data/<str:mon_server>', carrier_mon_server_data),
    path('api/carrier-monitorings', carr_mon_servers),
    path('api/carrier-monitorings/<str:pk>', carr_mon_server),
    path('api/carrier-monitoring-users', carr_mon_users),
    path('api/carrier-monitoring-users/<str:pk>', carr_mon_user),
]
