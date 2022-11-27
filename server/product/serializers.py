from rest_framework import serializers
from .models import Product
from massage.models import Massage
# from massage.serializers import MassageSerializer

class MyRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'info': obj.info,
        }


class ProductSerializer(serializers.ModelSerializer):
    massage_id = MyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

