from django.db import models


class Massage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=5000)
    image = models.ImageField(upload_to ='')

    def __str__(self):
        return self.name
