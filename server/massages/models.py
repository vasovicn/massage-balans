from django.db import models


class Massages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    info = models.CharField(max_length=200)
