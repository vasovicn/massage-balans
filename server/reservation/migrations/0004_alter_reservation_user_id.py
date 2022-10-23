# Generated by Django 4.1.2 on 2022-10-16 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_profile_phone_number'),
        ('reservation', '0003_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]