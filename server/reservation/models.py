from email.policy import default
from django.db import models
from masseur.models import Masseur
from massage.models import Massage
from user.models import Profile


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.CharField(max_length=200)
    massage_id = models.ForeignKey(Massage, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    masseur_id = models.ForeignKey(
        Masseur, on_delete=models.CASCADE, null=True)
    guest_name = models.CharField(max_length=200, default="", blank=True)
    guest_email = models.CharField(max_length=200, default="", blank=True)
    guest_phone = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return str(self.date) + ' ' + self.time
