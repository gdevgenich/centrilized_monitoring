from rest_framework import serializers
from .models import HPBXServer


class HPBXServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HPBXServer
        fields = ['id', 'short_name', 'api_fqdn', 'calls_fqdn']
