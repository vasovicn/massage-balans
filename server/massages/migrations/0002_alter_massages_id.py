# Generated by Django 4.1.2 on 2022-10-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massages',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]