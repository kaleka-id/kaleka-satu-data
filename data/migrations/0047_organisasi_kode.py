# Generated by Django 4.1.4 on 2023-03-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0046_lahanlegalitassertifikasi'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisasi',
            name='kode',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
    ]