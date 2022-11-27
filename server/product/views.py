from django.shortcuts import render
from product.models import Product
from product.serializers import ProductSerializer
from django.http import JsonResponse

def get(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True,)
    return JsonResponse(serializer.data,safe=False)