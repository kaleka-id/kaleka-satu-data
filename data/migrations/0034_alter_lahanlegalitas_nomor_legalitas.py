# Generated by Django 4.1.4 on 2023-02-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0033_wilayahdesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lahanlegalitas',
            name='nomor_legalitas',
            field=models.CharField(max_length=40),
        ),
    ]
