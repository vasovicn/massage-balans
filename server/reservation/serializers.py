from rest_framework import serializers

from masseur.serializers import MasseurSerializer
from massage.serializers import MassageSerializer
from user.serializers import ProfileSerializer
from .models import Reservation
class ReservationSerializer(serializers.ModelSerializer):
    masseur_id = MasseurSerializer()
    massage_id = MassageSerializer()
    user_id = ProfileSerializer()
    class Meta:
        model = Reservation
        fields = ['id', 'date', 'time', 'user_id','masseur_id', 'massage_id']
