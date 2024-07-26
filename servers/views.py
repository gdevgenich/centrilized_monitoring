from .models import HPBXServer
from .serializers import HPBXServerSerializer
from rest_framework import viewsets


class APIHPBXServers(viewsets.ModelViewSet):
    queryset = HPBXServer.objects.all()
    serializer_class = HPBXServerSerializer
