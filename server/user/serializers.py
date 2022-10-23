from rest_framework import serializers
from masseur.serializers import UserSerializer

from user.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'phone_number', 'location', 'birth_date', 'user']