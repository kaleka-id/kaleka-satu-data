# Generated by Django 4.1.4 on 2022-12-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0009_dictionary'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='perms_view',
            field=models.CharField(default='test', max_length=80, verbose_name='View Permission'),
            preserve_default=False,
        ),
    ]