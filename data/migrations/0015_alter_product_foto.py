# Generated by Django 4.1.4 on 2022-12-22 07:10

import data.dataset.testing
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_remove_shop_slug_remove_testing_slug_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='foto',
            field=models.FileField(upload_to='testing/', validators=[data.dataset.testing.file_image]),
        ),
    ]