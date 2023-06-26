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
from product.models import Product
import json
from .serializers import ReservationSerializer
from user.utils import Util

from django.views.decorators.csrf import csrf_exempt


def index(request):
    is_masseur = False
    if request.GET.get('date') and request.GET.get('masseur_id'):
        reservations_list = Reservation.objects.filter(date=request.GET.get('date'),
                                                       masseur_id=request.GET.get('masseur_id'), )
    elif request.GET.get('token'):
        token = Token.objects.get(key=request.GET.get('token'))
        if Masseur.objects.filter(user=token.user):
            masseur = Masseur.objects.get(user=token.user)
            reservations_list = Reservation.objects.filter(masseur_id=masseur)
            is_masseur = True
        else:
            reservations_list = Reservation.objects.filter(user_id=token.user.profile)
    else:
        reservations_list = Reservation.objects.all()

    reservations_list = reservations_list.order_by('date')
    serializer = ReservationSerializer(reservations_list, many=True, context={
        "request": request
    })
    return JsonResponse({'data': serializer.data, 'is_masseur': is_masseur}, safe=False)


def get(id):
    reservation = Reservation.objects.get(pk=id)
    serializer = ReservationSerializer(reservation)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def create(request):
    r = json.loads(request.body)
    masseur = Masseur.objects.get(id=r['masseur_id'])
    product_id = Product.objects.get(id=r['product_id']['id'])

    print('r', r)
    if r.get('client'):
        print('dasdasdas')
        reservation = Reservation(date=r['date'], time=r['time'], guest_name=r['client']['name'],
                                  guest_email=r['client']['email'], guest_phone=r['client']['phone'],
                                  masseur_id=masseur, product_id=product_id)
    elif r.get('token'):
        token = Token.objects.get(key=r['token'])
        reservation = Reservation(date=r['date'], time=r['time'], user_id=token.user.profile, masseur_id=masseur,
                                  product_id=product_id)
    else:
        reservation = Reservation(date=r['date'], time=r['time'], masseur_id=masseur, product_id=product_id)
    reservation.save()

    print('res', reservation.guest_email)
    client_email = reservation.guest_email if reservation.guest_email else reservation.user_id.user.email
    masseur_email = reservation.masseur_id.user.email
    email_body_masseur = 'Napravljena je nova rezervacija kod vas na datum %s u %sh' % (r['date'], r['time'])
    email_body_user = 'Vasa rezervacija je prihvacena. Vidimo se %s u %sh' % (r['date'], r['time'])
    data_masseur = {
        'email_body': email_body_masseur, 'to_email': masseur_email,
        'email_subject': 'Rezervacija masaze'
    }
    data_user = {
        'email_body': email_body_user, 'to_email': client_email,
        'email_subject': 'Rezervacija masaze'
    }
    Util.send_email(data_masseur)
    Util.send_email(data_user)
    return HttpResponse(status=200)


@csrf_exempt
def delete(request, id):
    reservation = Reservation.objects.get(id=id)
    client_email = reservation.guest_email if reservation.guest_email else reservation.user_id.user.email
    masseur_email = reservation.masseur_id.user.email
    email_body_masseur = 'Otkazana je rezervacija kod vas na datum %s u %sh' % (reservation.date, reservation.time)
    email_body_user = 'Vasa rezervacija %s u %sh je otkazana.' % (reservation.date, reservation.time)
    data_masseur = {
        'email_body': email_body_masseur, 'to_email': masseur_email,
        'email_subject': 'Rezervacija masaze'
    }
    data_user = {
        'email_body': email_body_user, 'to_email': client_email,
        'email_subject': 'Rezervacija masaze'
    }
    Util.send_email(data_masseur)
    Util.send_email(data_user)
    reservation.delete()
    return HttpResponse(status=200)
