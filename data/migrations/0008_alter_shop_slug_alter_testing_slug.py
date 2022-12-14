# Generated by Django 4.1.4 on 2022-12-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_testing_options_shop_slug_testing_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='testing',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
