# Generated by Django 4.1.4 on 2022-12-14 07:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20221208_1214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testing',
            options={'verbose_name': 'Testing - Deskripsi', 'verbose_name_plural': 'Testing - Deskripsi'},
        ),
        migrations.AddField(
            model_name='shop',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='testing',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='iucn',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326, verbose_name='Sebaran Geografis'),
        ),
    ]
