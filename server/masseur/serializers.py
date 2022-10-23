from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Masseur
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class MasseurSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Masseur
        fields = (
            "id",
            "user",
            "age",
            "info",
            "photo_url"
        )

    def get_photo_url(self, masseur):
        request = self.context.get('request')
        photo_url = masseur.image.url
        return request.build_absolute_uri(photo_url)
