from rest_framework import serializers
from .models import Massage
class MassageSerializer(serializers.ModelSerializer):
    # photo_url = serializers.SerializerMethodField()  
    class Meta:
        model = Massage
        fields = ['id', 'name', 'info', 'price', 'length', 'image']
        # fields = ['id', 'name', 'info', 'price', 'length', 'image_url', 'image']



    # def get_photo_url(self, massage):
    #     request = self.context.get('request')
    #     photo_url = massage.image.url
    #     return request.build_absolute_uri(photo_url)