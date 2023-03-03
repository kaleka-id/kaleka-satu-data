# Generated by Django 4.1.4 on 2023-03-03 09:20

import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0044_remove_catalogdocument_sheets_catalog_sheets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='sheets',
        ),
        migrations.AddField(
            model_name='catalog',
            name='google_sheets',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True, verbose_name=models.URLField()),
        ),
    ]