import imp
from django.shortcuts import render
from rest_framework.views import APIView
from masseur.models import Masseur
from masseur.serializers import MasseurSerializer
from rest_framework.response import Response
from django.http import JsonResponse


# Create your views here.


class MasseurList(APIView):
    def get(self, request, format=None):
        masseurs = Masseur.objects.all()
        serializer = MasseurSerializer(masseurs, many=True)
        return Response(serializer.data)


def index(request):
    messeurs_list = Masseur.objects.all()
    print('REQUEST', request)
    serializer = MasseurSerializer(messeurs_list, many=True)
    return JsonResponse(serializer.data, safe=False)
