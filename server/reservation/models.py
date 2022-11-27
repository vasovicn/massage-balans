from email.policy import default
from django.db import models
from masseur.models import Masseur
from user.models import Profile
from product.models import Product


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.CharField(max_length=200)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    masseur_id = models.ForeignKey(
        Masseur, on_delete=models.CASCADE, null=True)
    guest_name = models.CharField(max_length=200, default="", blank=True)
    guest_email = models.CharField(max_length=200, default="", blank=True)
    guest_phone = models.CharField(max_length=200, default="", blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.date) + ' ' + self.time
