# Generated by Django 4.1.4 on 2023-01-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0019_alter_profile_avatar_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(default='exist', editable=False, max_length=10),
        ),
    ]