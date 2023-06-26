from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Masseur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    info = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.user
