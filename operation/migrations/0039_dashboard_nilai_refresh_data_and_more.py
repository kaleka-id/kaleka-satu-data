# Generated by Django 4.1.4 on 2023-02-21 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0038_remove_activitylog_isp_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='nilai_refresh_data',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='satuan_refresh_data',
            field=models.CharField(choices=[('Realtime', 'Realtime'), ('Menit', 'Menit'), ('Jam', 'Jam'), ('Hari', 'Hari'), ('Minggu', 'Minggu'), ('Bulan', 'Bulan')], default='Hari', max_length=20),
            preserve_default=False,
        ),
    ]