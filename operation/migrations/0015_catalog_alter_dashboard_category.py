# Generated by Django 4.1.4 on 2022-12-27 03:41

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0014_alter_dashboard_category_alter_dashboard_height_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=40)),
                ('email_maintainer', models.CharField(max_length=40)),
                ('page_url', models.CharField(max_length=80, verbose_name='Page URL Path')),
                ('embed_url', models.CharField(max_length=100, verbose_name='Embed URL Path')),
                ('spreadsheet_url', models.CharField(max_length=100, verbose_name='Embed URL Path')),
                ('width', models.CharField(help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px", max_length=8)),
                ('height', models.CharField(help_text="Gunakan CSS unit seperti '%', 'cm', 'mm', 'in', 'px', 'pt', dan 'pc'. Contoh: 500px", max_length=8)),
                ('perms_view', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, null=True, size=None)),
            ],
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='category',
            field=models.CharField(choices=[('Static CSV', 'Static CSV'), ('Google Sheets', 'Google Sheets'), ('Google BigQuery', 'Google BigQuery'), ('Amazon Redshift', 'Amazon Redshift'), ('PostgreSQL Database', 'PostgreSQL Database'), ('MySQL Database', 'MySQL Database')], max_length=20),
        ),
    ]