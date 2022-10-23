# from email.message import Message
# import imp
from django.http import HttpResponse, JsonResponse
# from django.http import Http404
# from django.shortcuts import render
# from django.template import loader
from rest_framework.authtoken.models import Token

from masseur.models import Masseur
from massage.models import Massage

from .models import Reservation
import json
from .serializers import ReservationSerializer

from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.GET.get('date') and request.GET.get('masseur_id'):
        print(request.GET.get('masseur_id'))
        reservations_list = Reservation.objects.filter(date=request.GET.get('date'), masseur_id=request.GET.get('masseur_id'), )
        print(reservations_list)
    elif request.GET.get('token'):
        token = Token.objects.get(key=request.GET.get('token'))
        reservations_list = Reservation.objects.filter(user_id=token.user.profile)
    else:
        reservations_list = Reservation.objects.all()

    reservations_list = reservations_list.order_by('date')
    serializer = ReservationSerializer(reservations_list, many=True, context = {
   "request": request
})
    return JsonResponse(serializer.data,safe=False)

def get(id):
    reservation = Reservation.objects.get(pk=id)
    serializer = ReservationSerializer(reservation)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def create(request):
    r =json.loads(request.body)
    print(r)
    masseur = Masseur.objects.get(id=r['masseur_id'])
    massage = Massage.objects.get(name=r['type'])
    if r.get('client'):
        reservation = Reservation(date=r['date'], time=r['time'], guest_name = r['client']['name'], guest_email = r['client']['email'], guest_phone = r['client']['phone'], masseur_id=masseur, massage_id=massage,)
    elif r.get('token'):
       token = Token.objects.get(key=r['token'])
       reservation = Reservation(date=r['date'], time=r['time'], user_id = token.user.profile, masseur_id=masseur, massage_id=massage,)
    else:
        reservation = Reservation(date=r['date'], time=r['time'], massage_id=massage, masseur_id=masseur)
    reservation.save()
    return HttpResponse(status=200)

@csrf_exempt
def delete(request, id):
    reservation = Reservation.objects.get(id=id)
    reservation.delete()
    return HttpResponse(status=200)