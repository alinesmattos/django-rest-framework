from rest_framework import routers, serializers, viewsets
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'adress', 'age')

class EditClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client.history.model
        fields = '__all__'

