from oficina.models import Cars, Cliente
from rest_framework import serializers

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = []