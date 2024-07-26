from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import CarrierMonitoring, CarrierMonUser
from servers.models import HPBXServer
from .serializers import CarrierMonitoringSerializer, CarrierMonUserSerializer, CarrierMonServerDataSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import datetime
from zoneinfo import ZoneInfo


class CarrierMonitoringView(viewsets.ModelViewSet):
    queryset = CarrierMonitoring.objects.all()
    serializer_class = CarrierMonitoringSerializer

    def checked(self, request, pk):
        carrier_monitoring = get_object_or_404(CarrierMonitoring, pk=pk)
        carrier_monitoring.last_check = datetime.datetime.now(tz=ZoneInfo("UTC"))
        carrier_monitoring.save()
        return Response(status=status.HTTP_200_OK)

class CarrierMonUserView(viewsets.ModelViewSet):
    queryset = CarrierMonUser.objects.all()
    serializer_class = CarrierMonUserSerializer

    def get_users(self, *args):
        if self.request.GET.get("carrier") is None:
            carrier_mon_users = CarrierMonUser.objects.all()
        else:
            carrier_mon_users = CarrierMonUser.objects.filter(carrier_monitoring=self.request.GET.get("carrier"))
        carrier_mon_users = CarrierMonUserSerializer(carrier_mon_users, many=True)
        return JsonResponse(data=carrier_mon_users.data, safe=False)

    def create_mon_user(self, *args):
        if self.request.data.get("carrier_monitoring") is not None:
            carrier_monitoring = get_object_or_404(CarrierMonitoring, pk=self.request.data.get("carrier_monitoring"))
        else:
            carrier_monitoring = None
        hpbx_server = get_object_or_404(HPBXServer, pk=self.request.data.get("hpbx_server"))
        carrier_mon_user = CarrierMonUser()
        carrier_mon_user.carrier_monitoring = carrier_monitoring
        carrier_mon_user.hpbx_server = hpbx_server
        carrier_mon_user.user_name = self.request.data.get("user_name")
        carrier_mon_user.device_id = self.request.data.get("device_id")
        carrier_mon_user.password = self.request.data.get("password")
        carrier_mon_user.phone_number = self.request.data.get("phone_number")
        carrier_mon_user.save()
        return Response(status=status.HTTP_201_CREATED)

    def update_mon_user(self, *args, **kwargs):
        carrier_mon_user = get_object_or_404(CarrierMonUser, pk=self.kwargs['pk'])
        hpbx_server = get_object_or_404(HPBXServer, pk=self.request.data.get("hpbx_server"))
        if self.request.data.get("carrier_monitoring") is not None:
            carrier_monitoring = get_object_or_404(CarrierMonitoring, pk=self.request.data.get("carrier_monitoring"))
        else:
            carrier_monitoring = None
        carrier_mon_user.carrier_monitoring = carrier_monitoring
        carrier_mon_user.hpbx_server = hpbx_server
        carrier_mon_user.user_name = self.request.data.get("user_name")
        carrier_mon_user.device_id = self.request.data.get("device_id")
        carrier_mon_user.password = self.request.data.get("password")
        carrier_mon_user.phone_number = self.request.data.get("phone_number")
        carrier_mon_user.save()
        return Response(status=status.HTTP_200_OK)

class CarrierMonServerData(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarrierMonServerDataSerializer

    def get_queryset(self):
        query_set = CarrierMonitoring.objects.filter(mon_server=self.kwargs['mon_server'], active=True)
        return query_set


