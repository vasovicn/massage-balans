# Generated by Django 4.1.2 on 2022-10-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_alter_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest_email',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_phone',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
