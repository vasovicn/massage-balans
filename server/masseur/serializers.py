from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Masseur
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class MasseurSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Masseur
        fields = (
            "id",
            "user",
            "age",
            "info",
        )
