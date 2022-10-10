# from email.message import Message
# import imp
from django.http import HttpResponse, JsonResponse
# from django.http import Http404
# from django.shortcuts import render
# from django.template import loader

from .models import Reservation
import json
from .serializers import ReservationSerializer

from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.GET.get('date'):
        reservations_list = Reservation.objects.filter(date=request.GET.get('date'))
    else:
        reservations_list = Reservation.objects.all()
    serializer = ReservationSerializer(reservations_list, many=True)
    return JsonResponse(serializer.data,safe=False)

def get(id):
    reservation = Reservation.objects.get(pk=id)
    serializer = ReservationSerializer(reservation)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def create(request):
    r =json.loads(request.body)
    reservation = Reservation(date=r['date'], time=r['time'], type = r['type'], length = r['length'])
    reservation.save()
    return HttpResponse(status=200)