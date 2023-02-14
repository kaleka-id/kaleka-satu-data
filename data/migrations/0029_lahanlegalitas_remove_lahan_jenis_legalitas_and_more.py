# Generated by Django 4.1.4 on 2023-02-09 03:10

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0028_product_keterangan_product_status_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LahanLegalitas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('jenis_legalitas', models.CharField(blank=True, choices=[('Hak Milik', 'Hak Milik'), ('Hak Sewa', 'Hak Sewa'), ('Hak Guna Lahan', 'Hak Guna Lahan'), ('Hak Guna Bangunan', 'Hak Guna Bangunan'), ('Girik', 'Girik'), ('Surat Keterangan Tanah', 'Surat Keterangan Tanah'), ('Tanah Adat', 'Tanah Adat'), ('Tanpa Status', 'Tidak ada Status (Komunal)')], max_length=25, null=True)),
                ('nomor_legalitas', models.CharField(max_length=20)),
                ('luas_pada_dokumen', models.DecimalField(decimal_places=2, help_text='Satuan dalam Ha, jika satuannya lain mohon dikonversi terlebih dahulu', max_digits=10)),
                ('tahun_legalitas', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1900)])),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation', max_length=20)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Legalitas Lahan',
                'verbose_name_plural': 'Legalitas Lahan',
                'permissions': [('search_lahanlegalitas', 'Can search Legalitas Lahan in Dictionary')],
            },
        ),
        migrations.RemoveField(
            model_name='lahan',
            name='jenis_legalitas',
        ),
        migrations.RemoveField(
            model_name='lahan',
            name='nomor_legalitas',
        ),
        migrations.RemoveField(
            model_name='lahan',
            name='tahun_legalitas',
        ),
        migrations.AddField(
            model_name='lahan',
            name='keterangan',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lahan',
            name='status_data',
            field=models.CharField(choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation', max_length=20),
        ),
        migrations.AlterField(
            model_name='lahan',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326, verbose_name='Lahan'),
        ),
        migrations.AlterField(
            model_name='lahan',
            name='petani',
            field=models.ForeignKey(blank=True, help_text='Gunakan tabel <a target="blank" href="/dict/orang/">Orang</a> sebagai referensi untuk mengisi bagian ini', null=True, on_delete=django.db.models.deletion.CASCADE, to='data.orang'),
        ),
        migrations.CreateModel(
            name='LahanLegalitasSTDB',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nomor_dokumen', models.CharField(max_length=20)),
                ('tahun_dokumen', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1900)])),
                ('status_dokumen', models.CharField(choices=[('Berlaku', 'Berlaku'), ('Tidak Berlaku', 'Tidak Berlaku')], max_length=20)),
                ('jumlah_pohon', models.IntegerField()),
                ('tahun_tanam', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1900)])),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation', max_length=20)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('legalitas_lahan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.lahanlegalitas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Legalitas Lahan - Dokumen STDB ',
                'verbose_name_plural': 'Legalitas Lahan - Dokumen STDB',
                'permissions': [('search_lahanlegalitasstdb', 'Can search Legalitas Lahan - Dokumen STDB in Dictionary')],
            },
        ),
        migrations.CreateModel(
            name='LahanLegalitasLingkungan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('jenis_dokumen', models.CharField(blank=True, choices=[('SPPL', 'SPPL (Surat Pernyataan Pengelolaan Lingkungan)'), ('UKL-UPL', 'Upaya Pengelolaan Lingkungan dan Upaya Pemantauan Lingkungan Hidup (UKL-UPL)'), ('AMDAL', 'Analisis Mengenai Dampak Lingkungan (AMDAL)')], max_length=20, null=True)),
                ('nomor_dokumen', models.CharField(max_length=20)),
                ('tahun_dokumen', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1900)])),
                ('status_dokumen', models.CharField(choices=[('Berlaku', 'Berlaku'), ('Tidak Berlaku', 'Tidak Berlaku')], max_length=20)),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation', max_length=20)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('legalitas_lahan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.lahanlegalitas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Legalitas Lahan - Dokumen Lingkungan ',
                'verbose_name_plural': 'Legalitas Lahan - Dokumen Lingkungan',
                'permissions': [('search_lahanlegalitaslingkungan', 'Can search Legalitas Lahan - Dokumen Lingkungan in Dictionary')],
            },
        ),
        migrations.AddField(
            model_name='lahan',
            name='legalitas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.lahanlegalitas'),
        ),
    ]