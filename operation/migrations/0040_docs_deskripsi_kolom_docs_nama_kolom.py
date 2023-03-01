# Generated by Django 4.1.4 on 2023-02-28 02:15

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0039_dashboard_nilai_refresh_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='deskripsi_kolom',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(max_length=30), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='docs',
            name='nama_kolom',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=None),
        ),
    ]