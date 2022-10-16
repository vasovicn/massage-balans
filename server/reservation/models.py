from email.policy import default
from django.db import models
from user.models import Profile

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    length = models.IntegerField(default=0)
    type = models.CharField(max_length=200, default="")
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    guest_name = models.CharField(max_length=200, default="")
    guest_email = models.CharField(max_length=200, default="")
    guest_phone = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.date + ' ' + self.time