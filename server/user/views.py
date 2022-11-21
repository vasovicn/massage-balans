from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from rest_framework.authtoken.models import Token
import json
import braintree
from user.serializers import ProfileSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer

from user.models import Profile

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework.generics import GenericAPIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, force_bytes, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from rest_framework.permissions import AllowAny


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
    username = request.GET.get('username')
    if username:
        email = User.objects.filter(username=username).values('email')
        if email:
            return HttpResponse(email[0]['email'], status=200)
        else:
            return HttpResponse(status=404)
    if not token:
        return JsonResponse({})
    user = User.objects.get(auth_token=token)
    profile = Profile.objects.get(user=user)
    serializer = ProfileSerializer(profile)
    return JsonResponse(serializer.data)


@csrf_exempt
def verify_password(request):
    token = json.loads(request.body)['token']
    old_password = json.loads(request.body)['oldPassword']
    new_password = json.loads(request.body)['newPassword']

    user = User.objects.get(auth_token=token)
    user = auth.authenticate(username=user.username, password=old_password)
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
    profile.update(phone_number=phone_number,
                   location=location, birth_date=birth_date)
    serializer = ProfileSerializer(profile[0])

    return JsonResponse(serializer.data)


class RequestPasswordResetEmail(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordEmailRequestSerializer

    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if User.objects.get(email=request.data['params']['email']):
            user = User.objects.get(email=request.data['params']['email'])
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            absurl = 'http://' + current_site + \
                '/user/password-reset-confirm/' + uidb64 + '/' + token
            email_body = 'Hello, \nUse link bellow to reset password \n' + absurl
            data = {
                'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Reset your password'
            }
            Util.send_email(data)
        return JsonResponse({'success': 'We have send link to reset password'}, status=200)


def get_reset_password(self, uidb64, token):
    id = smart_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=id)
    if not PasswordResetTokenGenerator().check_token(user, token):
        return render(self, 'email_template.html')
    else:
        return redirect('http://localhost:8080/massage-reservations/%s/%s' % (uidb64, token), body={'success': True, 'message': 'Credentials Valid', 'uidb64': uidb64, 'token': token})


class SetNewpasswordAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data['params']['body'])

        serializer.is_valid(raise_exception=True)
        return JsonResponse({'success': True, 'message': 'Success'})