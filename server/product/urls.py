from django.urls import path

from . import views
from rest_framework import routers
from django.urls import path, include
from . import views
router = routers.DefaultRouter()
# router.register(r'messsages', views.MassageViewSet)

urlpatterns = [
    path("", views.get, name='get'),
]