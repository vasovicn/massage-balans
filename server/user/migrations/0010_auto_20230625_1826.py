from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_profile_phone_number'),
        # Add other dependencies if needed
    ]

    operations = [
        migrations.RunSQL(
            'CREATE UNIQUE INDEX unique_user_email ON auth_user(email) WHERE email IS NOT NULL;',
            'DROP INDEX unique_user_email;'
        ),
    ]