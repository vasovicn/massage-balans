from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
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