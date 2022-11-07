from django.urls import path

from . import views
from rest_framework import routers
from django.urls import path, include
from . import views
from .views import RequestPasswordResetEmail, SetNewpasswordAPIView
router = routers.DefaultRouter()
# router.register(r'messsages', views.MassageViewSet)

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.get, name="get"),
    path('update', views.update, name="update"),
    path('verify_password', views.verify_password, name='verify_password'),
    path('request-reset-email', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('password-reset-confirm/<uidb64>/<token>/', views.get_reset_password, name='get_reset_password'),
    path('password-reset-complete', SetNewpasswordAPIView.as_view(), name='password-reset-complete')
]
