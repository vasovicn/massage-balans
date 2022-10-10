from rest_framework import serializers
from .models import Massage
class MassageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')    
    class Meta:
        model = Massage
        fields = ['id', 'name', 'info', 'price', 'length', 'image_url', 'image']


    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        return request.build_absolute_uri(image_url)