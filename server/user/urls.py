from django.urls import path

from . import views
from rest_framework import routers
from django.urls import path, include
from . import views
router = routers.DefaultRouter()
# router.register(r'messsages', views.MassageViewSet)

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.get, name="get"),
    path('update', views.update, name="update"),
    path('verify_password', views.verify_password, name='verify_password')
]
