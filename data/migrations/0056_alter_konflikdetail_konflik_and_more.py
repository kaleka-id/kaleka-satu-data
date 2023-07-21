# Generated by Django 4.1.4 on 2023-04-14 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0055_konflikdetail_konflik_konflikpelapor_konflik_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konflikdetail',
            name='konflik',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.konflik'),
        ),
        migrations.AlterField(
            model_name='konflikpelapor',
            name='konflik',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.konflik'),
        ),
        migrations.AlterField(
            model_name='konflikterlapor',
            name='konflik',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.konflik'),
        ),
    ]