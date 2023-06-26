from email.policy import default
from django.db import models
from massage.models import Massage


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    massage_id = models.ForeignKey(Massage, on_delete=models.CASCADE, null=True, related_name='products')
    # massage_name = models.CharField()

    def __str__(self):
        return '%s %sdin %smin' % (self.massage_id.name, self.price, self.length)
