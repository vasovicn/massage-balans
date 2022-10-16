from email.message import Message
import imp
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.shortcuts import render
from django.template import loader

from django.conf import settings

from .models import Massage
from .forms import NameForm
import json
from .serializers import MassageSerializer

from django.views.decorators.csrf import csrf_exempt

def index(request):
    messages_list = Massage.objects.all()
    serializer = MassageSerializer(messages_list, many=True)
    print('ROOT' + settings.MEDIA_ROOT)
    print('URL' + settings.MEDIA_URL)
    return JsonResponse(serializer.data,safe=False)

def get(request, id):
    massage = Massage.objects.get(pk=id)
    template = loader.get_template('massage/detail.html')
    context = {
        'massage': massage,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def create(request):
    r =json.loads(request.body)
    massage = Massage(name=r['name'], info=r['info'], price = r['price'], length = r['length'], image = r['image'])
    massage.save()
    return HttpResponse(status=200)