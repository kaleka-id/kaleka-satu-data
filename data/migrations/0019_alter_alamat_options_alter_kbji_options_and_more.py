# Generated by Django 4.1.4 on 2023-01-11 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_alter_alamat_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alamat',
            options={'permissions': [('search_alamat', 'Can search Alamat in Dictionary')], 'verbose_name': 'Alamat', 'verbose_name_plural': 'Alamat'},
        ),
        migrations.AlterModelOptions(
            name='kbji',
            options={'permissions': [('search_kbji', 'Can search KBJI in Dictionary')], 'verbose_name': 'Klasifikasi Baku Jabatan', 'verbose_name_plural': 'Klasifikasi Baku Jabatan'},
        ),
        migrations.AlterModelOptions(
            name='orang',
            options={'permissions': [('search_orang', 'Can search Orang in Dictionary')], 'verbose_name': 'Orang', 'verbose_name_plural': 'Orang'},
        ),
        migrations.AlterModelOptions(
            name='profesi',
            options={'permissions': [('search_profesi', 'Can search Profesi in Dictionary')], 'verbose_name': 'Profesi', 'verbose_name_plural': 'Profesi'},
        ),
    ]
