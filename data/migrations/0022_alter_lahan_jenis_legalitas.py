# Generated by Django 4.1.4 on 2023-01-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_alter_lahan_options_alter_lahan_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lahan',
            name='jenis_legalitas',
            field=models.CharField(blank=True, choices=[('Hak Milik', 'Hak Milik'), ('Hak Sewa', 'Hak Sewa'), ('Hak Guna Lahan', 'Hak Guna Lahan'), ('Hak Guna Bangunan', 'Hak Guna Bangunan'), ('Girik', 'Girik'), ('Surat Keterangan Tanah', 'Surat Keterangan Tanah'), ('Tanah Adat', 'Tanah Adat'), ('Tanpa Status', 'Tidak ada Status (Komunal)')], max_length=25, null=True),
        ),
    ]
