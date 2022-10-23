from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from masseur import views

# from . import views
# from rest_framework import routers
# from django.urls import path, include
# from . import views
# router = routers.DefaultRouter()
# # router.register(r'messsages', views.MassageViewSet)

urlpatterns = [
    path('', views.index),
]
