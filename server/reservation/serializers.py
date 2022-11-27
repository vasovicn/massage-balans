from rest_framework import serializers

from masseur.serializers import MasseurSerializer
from user.serializers import ProfileSerializer
from product.serializers import ProductSerializer
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    masseur_id = MasseurSerializer()
    user_id = ProfileSerializer()
    product_id = ProductSerializer()
    class Meta:
        model = Reservation
        fields = ['id', 'date', 'time', 'user_id','masseur_id', 'product_id']
