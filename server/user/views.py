from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from rest_framework.authtoken.models import Token
import json


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

def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def verifyPassword(requsts):
    token = request.body.token
    oldPassword = request.body.odlPassword

    user = User.objects.get(key=token)
    user = auth.authenticate(username=user.username, password=oldPassword)

    if user:
        return HttpResponse(status=200)
    return HttpResponse(status=404)