import os

from rest_framework import serializers
from .models import Massage
from django.conf import settings
from product.serializers import ProductSerializer

class MassageSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Massage
        fields = '__all__'

    def get_photo_url(self, massage):
        request = self.context.get('request')
        photo_url = massage.image.url
        return request.build_absolute_uri(photo_url)

