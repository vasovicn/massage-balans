from rest_framework import serializers
from .models import Massages
class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massages
        fields = ['id', 'name', 'info', 'price']