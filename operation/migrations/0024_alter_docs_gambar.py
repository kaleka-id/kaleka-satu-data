# Generated by Django 4.1.4 on 2023-01-26 02:51

from django.db import migrations, models
import operation.ops_models.docs


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0023_alter_webentry_options_webentry_browser_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='gambar',
            field=models.FileField(upload_to=operation.ops_models.docs.Docs.get_filename),
        ),
    ]