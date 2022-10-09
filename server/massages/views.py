from email.message import Message
import imp
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.shortcuts import render
from django.template import loader

from .models import Massages
from .forms import NameForm
import json
from .serializers import MassageSerializer

from django.views.decorators.csrf import csrf_exempt

def index(request):
    print('get')
    messages_list = Massages.objects.all()
    print(messages_list)
    serializer = MassageSerializer(messages_list, many=True)
    print(serializer)
    return JsonResponse(serializer.data,safe=False)

def get(request, id):
    print("GET")
    massage = Massages.objects.get(pk=id)
    print(massage)
    template = loader.get_template('massages/detail.html')
    context = {
        'massage': massage,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def create(request):
    print(request.body)
    r =json.loads(request.body)
    print(r)
    massage = Massages(name=r['name'], info=r['info'], price = r['price'], length = r['length'], image = r['image'])
    massage.save()
    print("sacuvano")
    return HttpResponse(status=200)