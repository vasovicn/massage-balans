from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from rest_framework.authtoken.models import Token
import json
from user.serializers import ProfileSerializer

from user.models import Profile


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = json.loads(request.body)['username']
        password = json.loads(request.body)['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/admin/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')


def get(request):
    token = request.GET.get('token')
    if not token:
        return JsonResponse({})
    user = User.objects.get(auth_token=token)
    profile = Profile.objects.get(user=user)
    serializer = ProfileSerializer(profile)
    return JsonResponse(serializer.data)


@csrf_exempt
def verifyPassword(request):
    token = json.loads(request.body)['token']
    old_password = json.loads(request.body)['oldPassword']
    new_password = json.loads(request.body)['newPassword']

    user = User.objects.get(auth_token=token)
    user = auth.authenticate(username=user.username, password=old_password)
    print(user)
    if user:
        user.set_password(new_password)
        user.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)


@csrf_exempt
def update(request):
    token = json.loads(request.body)['params']['token']
    phone_number = json.loads(request.body)['body']['phone_number']
    location = json.loads(request.body)['body']['location']
    birth_date = json.loads(request.body)['body']['birth_date']
    first_name = json.loads(request.body)['body']['user']['first_name']
    last_name = json.loads(request.body)['body']['user']['last_name']
    email = json.loads(request.body)['body']['user']['email']
    
    user = User.objects.filter(auth_token=token)
    user.update(first_name=first_name, last_name=last_name, email=email)
    profile = Profile.objects.filter(user=user[0])
    profile.update(phone_number=phone_number, location=location, birth_date=birth_date)
    serializer = ProfileSerializer(profile[0])
    return JsonResponse(serializer.data)