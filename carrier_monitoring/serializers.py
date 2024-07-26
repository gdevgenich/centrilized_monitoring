from rest_framework import serializers
from .models import CarrierMonitoring, CarrierMonUser


class CarrierMonitoringSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarrierMonitoring
        fields = ['id', 'name', 'carrier', 'mon_server', 'last_check', 'active', 'alert']


class CarrierMonUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarrierMonUser
        fields = ['id', 'carrier_monitoring', 'hpbx_server', 'user_name', 'device_id', 'password', 'phone_number']
        depth = 1


class CarrierMonUserSerializerShort(serializers.ModelSerializer):

    class Meta:
        model = CarrierMonUser
        fields = ['hpbx_server', 'user_name', 'device_id', 'password', 'phone_number']
        depth = 1


class CarrierMonServerDataSerializer(serializers.ModelSerializer):
    users = CarrierMonUserSerializerShort(many=True, read_only=True)

    class Meta:
        model = CarrierMonitoring
        fields = ['id', 'name', 'carrier', 'mon_server', 'last_check', 'active', 'users']
