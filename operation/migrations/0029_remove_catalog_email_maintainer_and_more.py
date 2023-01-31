# Generated by Django 4.1.4 on 2023-01-31 03:05

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('operation', '0028_request_status_alter_request_request_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='email_maintainer',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='embed_url',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='height',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='page_url',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='perms_view',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='spreadsheet_url',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='width',
        ),
        migrations.AddField(
            model_name='catalog',
            name='documents_document',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True, verbose_name=models.URLField()),
        ),
        migrations.AddField(
            model_name='catalog',
            name='documents_portable',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True, verbose_name=models.URLField()),
        ),
        migrations.AddField(
            model_name='catalog',
            name='documents_ppresentation',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True, verbose_name=models.URLField()),
        ),
        migrations.AddField(
            model_name='catalog',
            name='email_maintainers',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.URLField(), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='catalog',
            name='permission_view',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='spreadsheets_download',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True, verbose_name=models.URLField()),
        ),
        migrations.AddField(
            model_name='catalog',
            name='spreadsheets_link',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True, verbose_name=models.URLField()),
        ),
    ]