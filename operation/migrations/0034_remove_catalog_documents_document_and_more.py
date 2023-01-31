# Generated by Django 4.1.4 on 2023-01-31 09:23

import data.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0033_remove_dashboard_email_maintainer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='documents_document',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='documents_portable',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='documents_presentation',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='spreadsheets_download',
        ),
        migrations.CreateModel(
            name='CatalogDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to='catalog/word', validators=[data.validators.file_doc])),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation.catalog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]