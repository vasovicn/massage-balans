import os

from rest_framework import serializers
from .models import Massage
from django.conf import settings

class MassageSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Massage
        # image_url 
        fields = ['id', 'name', 'info', 'price', 'length', 'photo_url']
        # fields = ['id', 'name', 'info', 'price', 'length', 'image_url', 'image']

    def get_photo_url(self, massage):
        request = self.context.get('request')
        photo_url = massage.image.url
        return request.build_absolute_uri(photo_url)