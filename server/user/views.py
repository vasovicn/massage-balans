from django.http import HttpResponse
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