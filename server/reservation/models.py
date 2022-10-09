from django.db import models


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200, default=0)
    length = models.IntegerField(default=0)
    type = models.CharField(max_length=200, default="")
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)