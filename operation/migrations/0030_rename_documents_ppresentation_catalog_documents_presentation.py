# Generated by Django 4.1.4 on 2023-01-31 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0029_remove_catalog_email_maintainer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='documents_ppresentation',
            new_name='documents_presentation',
        ),
    ]
