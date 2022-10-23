# from email.message import Message
# import imp
from django.http import HttpResponse, JsonResponse
# from django.http import Http404
# from django.shortcuts import render
# from django.template import loader
from rest_framework.authtoken.models import Token

from .models import Reservation
import json
from .serializers import ReservationSerializer

from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.GET.get('date'):
        reservations_list = Reservation.objects.filter(date=request.GET.get('date'))
    elif request.GET.get('token'):
        token = Token.objects.get(key=request.GET.get('token'))
        reservations_list = Reservation.objects.filter(user_id=token.user.profile)
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
    print(r)
    if r.get('client'):
        reservation = Reservation(date=r['date'], time=r['time'], type = r['type'], length = r['length'], guest_name = r['client']['name'], guest_email = r['client']['email'], guest_phone = r['client']['phone'])
    elif r.get('token'):
       token = Token.objects.get(key=r['token'])
       reservation = Reservation(date=r['date'], time=r['time'], type = r['type'], length = r['length'], user_id = token.user.profile)
    else:
        reservation = Reservation(date=r['date'], time=r['time'], type = r['type'], length = r['length'])
    reservation.save()
    return HttpResponse(status=200)