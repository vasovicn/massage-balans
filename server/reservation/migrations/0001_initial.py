# Generated by Django 4.1.2 on 2022-10-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=200)),
                ('time', models.CharField(default=0, max_length=200)),
                ('length', models.IntegerField(default=0)),
                ('type', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
