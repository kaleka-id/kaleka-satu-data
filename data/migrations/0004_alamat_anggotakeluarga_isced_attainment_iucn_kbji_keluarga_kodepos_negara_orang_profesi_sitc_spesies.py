# Generated by Django 3.2.16 on 2022-12-07 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0003_rename_name_shop_name_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alamat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kode_prov', models.CharField(max_length=2, verbose_name='Kode Provinsi')),
                ('nama_prov', models.CharField(help_text="Tuliskan nama provinsi tanpa imbuhan 'Provinsi', 'Prov.' dsb. Tulisan akan otomatis terkonversi menjadi huruf kapital.", max_length=30, verbose_name='Nama Provinsi')),
                ('kode_kabkot', models.CharField(max_length=4, verbose_name='Kode Kabupaten/Kota')),
                ('nama_kabkot', models.CharField(help_text="Tuliskan nama kabupaten tanpa imbuhan 'Kabupaten', 'Kab.' dsb. Untuk nama kota, gunakan imbuhan 'Kota'. Tulisan akan otomatis terkonversi menjadi huruf kapital.", max_length=30, verbose_name='Nama Kabupaten/Kota')),
                ('kode_kec', models.CharField(max_length=6, verbose_name='Kode Kecamatan')),
                ('nama_kec', models.CharField(help_text="Tuliskan nama kecamatan tanpa imbuhan 'Kecamatan', 'Kec.' dsb. Tulisan akan otomatis terkonversi menjadi huruf kapital.", max_length=40, verbose_name='Nama Kecamatan')),
                ('kode_desa', models.CharField(max_length=10, unique=True, verbose_name='Kode Desa/Kelurahan')),
                ('nama_desa', models.CharField(help_text="Tuliskan nama desa tanpa imbuhan 'Desa', 'Ds.' dsb. Untuk nama kelurahan, gunakan imbuhan 'Kel.'. Tulisan akan otomatis terkonversi menjadi huruf kapital.", max_length=40, verbose_name='Nama Desa/Kelurahan')),
                ('dasar_hukum', models.CharField(max_length=30, verbose_name='Dasar Hukum')),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Alamat',
                'verbose_name_plural': 'Alamat',
            },
        ),
        migrations.CreateModel(
            name='KBJI',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kode_gol_pokok', models.CharField(max_length=1, verbose_name='Kode Golongan Pokok')),
                ('golongan_pokok', models.CharField(help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.', max_length=100, verbose_name='Nama Golongan Pokok')),
                ('kode_subgol_pokok', models.CharField(max_length=2, verbose_name='Kode Sub-Golongan Pokok')),
                ('subgolongan_pokok', models.CharField(help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.', max_length=100, verbose_name='Nama Sub-Golongan Pokok')),
                ('kode_gol', models.CharField(max_length=3, verbose_name='Kode Golongan')),
                ('golongan', models.CharField(help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.', max_length=100, verbose_name='Nama Golongan')),
                ('kode_subgol', models.CharField(max_length=4, verbose_name='Kode Sub-Golongan')),
                ('subgolongan', models.CharField(help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.', max_length=100, verbose_name='Nama Sub-Golongan')),
                ('kode_jabatan', models.DecimalField(decimal_places=2, max_digits=6, unique=True, verbose_name='Kode Jabatan')),
                ('jabatan', models.CharField(help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.', max_length=100, verbose_name='Nama Jabatan')),
                ('dasar_hukum', models.CharField(max_length=120)),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Klasifikasi Baku Jabatan',
                'verbose_name_plural': 'Klasifikasi Baku Jabatan',
            },
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kode', models.CharField(max_length=5)),
                ('nama', models.CharField(max_length=30)),
                ('deskripsi', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Testing Data',
                'verbose_name_plural': 'Testing Data',
            },
        ),
        migrations.CreateModel(
            name='Spesies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_indonesia', models.CharField(blank=True, max_length=50)),
                ('nama_inggris', models.CharField(blank=True, max_length=50)),
                ('kingdom', models.CharField(max_length=50)),
                ('phylum', models.CharField(max_length=50)),
                ('Class', models.CharField(max_length=50)),
                ('order', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('genus', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=100)),
                ('dasar_hukum', models.CharField(max_length=60)),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Klasifikasi Baku Spesies',
                'verbose_name_plural': 'Klasifikasi Baku Spesies',
            },
        ),
        migrations.CreateModel(
            name='SITC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kode_section', models.CharField(max_length=1)),
                ('kode_division', models.CharField(max_length=2)),
                ('kode_group', models.CharField(max_length=3)),
                ('kode_subgroup', models.CharField(max_length=5)),
                ('kode_heading', models.CharField(max_length=6)),
                ('deskripsi_section', models.TextField()),
                ('deskripsi_division', models.TextField()),
                ('deskripsi_group', models.TextField()),
                ('deskripsi_subgroup', models.TextField()),
                ('deskripsi_heading', models.TextField()),
                ('dasar_hukum', models.CharField(max_length=120)),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Klasifikasi Baku Komoditas',
                'verbose_name_plural': 'Klasifikasi Baku Komoditas',
            },
        ),
        migrations.CreateModel(
            name='Profesi',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kode_kbji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.kbji')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profesi',
                'verbose_name_plural': 'Profesi',
            },
        ),
        migrations.CreateModel(
            name='Orang',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nik', models.PositiveBigIntegerField(unique=True, verbose_name='Nomor Induk Kependudukan')),
                ('nama_lengkap', models.CharField(help_text='Nama sesuai KTP, tidak ditambahkan gelar.', max_length=50)),
                ('jenis_kelamin', models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=9)),
                ('tempat_lahir', models.CharField(help_text='Tulisan akan otomatis terkonversi menjadi huruf kapital.', max_length=30)),
                ('tanggal_lahir', models.DateField()),
                ('status_kawin', models.CharField(choices=[('Belum Kawin', 'Belum Kawin'), ('Kawin', 'Kawin'), ('Cerai Hidup', 'Cerai Hidup'), ('Cerai Mati', 'Cerai Mati')], max_length=11)),
                ('rt', models.PositiveSmallIntegerField(verbose_name='RT')),
                ('rw', models.PositiveSmallIntegerField(verbose_name='RW')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alamat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.alamat')),
                ('profesi', models.ManyToManyField(to='data.Profesi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Orang',
                'verbose_name_plural': 'Orang',
            },
        ),
        migrations.CreateModel(
            name='Negara',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_singkat', models.CharField(max_length=100)),
                ('nama_resmi', models.CharField(max_length=100)),
                ('region_pbb', models.CharField(choices=[('Africa', 'Africa'), ('Americas', 'Americas'), ('Antarctica', 'Antarctica'), ('Asia', 'Asia'), ('Europe', 'Europe'), ('Oceania', 'Oceania')], max_length=15, verbose_name='Region PBB')),
                ('subregion', models.CharField(choices=[('Antarctica', 'Antarctica'), ('Australia and New Zealand', 'Australia and New Zealand'), ('Caribbean', 'Caribbean'), ('Central America', 'Central America'), ('Central Asia', 'Central Asia'), ('Eastern Africa', 'Eastern Africa'), ('Eastern Asia', 'Eastern Asia'), ('Eastern Europe', 'Eastern Europe'), ('Melanesia', 'Melanesia'), ('Micronesia', 'Micronesia'), ('Middle Africa', 'Middle Africa'), ('Northern Africa', 'Northern Africa'), ('Northern America', 'Northern America'), ('Northern Europe', 'Northern Europe'), ('Polynesia', 'Polynesia'), ('Seven seas (open ocean)', 'Seven seas (open ocean)'), ('South America', 'South America'), ('South-Eastern Asia', 'South-Eastern Asia'), ('Southern Africa', 'Southern Africa'), ('Southern Asia', 'Southern Asia'), ('Southern Europe', 'Southern Europe'), ('Western Africa', 'Western Africa'), ('Western Asia', 'Western Asia'), ('Western Europe', 'Western Europe')], max_length=30)),
                ('region_wb', models.CharField(choices=[('Antarctica', 'Antarctica'), ('East Asia & Pacific', 'East Asia & Pacific'), ('Europe & Central Asia', 'Europe & Central Asia'), ('Latin America & Caribbean', 'Latin America & Caribbean'), ('Middle East & North Africa', 'Middle East & North Africa'), ('North America', 'North America'), ('South Asia', 'South Asia'), ('Sub-Saharan Africa', 'Sub-Saharan Africa')], max_length=30, verbose_name='Region World Bank')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dasar_hukum', models.CharField(max_length=120)),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Negara',
                'verbose_name_plural': 'Negara',
            },
        ),
        migrations.CreateModel(
            name='KodePos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kode', models.CharField(max_length=5)),
                ('dasar_hukum', models.CharField(max_length=30, verbose_name='Dasar Hukum')),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alamat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.alamat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kode Pos',
                'verbose_name_plural': 'Kode Pos',
            },
        ),
        migrations.CreateModel(
            name='Keluarga',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nkk', models.PositiveBigIntegerField(unique=True, verbose_name='Nomor Kartu Kependudukan')),
                ('rt', models.PositiveSmallIntegerField(verbose_name='RT')),
                ('rw', models.PositiveSmallIntegerField(verbose_name='RW')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alamat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.alamat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Keluarga',
                'verbose_name_plural': 'Keluarga',
            },
        ),
        migrations.CreateModel(
            name='IUCN',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kategori', models.CharField(choices=[('NE', 'Not Evaluated'), ('DD', 'Data Deficient'), ('LC', 'Least Concern'), ('NT', 'Near Threatened'), ('VU', 'Vulnerable'), ('EN', 'Endangered'), ('CR', 'Critically Endangered'), ('EW', 'Extinct in the Wild'), ('EX', 'Extinct')], max_length=2)),
                ('tanggal_asesmen', models.DateField()),
                ('referensi_asesmen', models.TextField()),
                ('lokasi_geografis', models.TextField(blank=True, help_text='Saat ini tolong diisikan dengan koordinat Well-known Text (WKT) Geografis WGS84. Ke depan akan diganti dengan fitur digitasi spasial')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('habitat_asal', models.ManyToManyField(to='data.Negara')),
                ('spesies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.spesies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'IUCN Red List',
                'verbose_name_plural': 'IUCN Red List',
            },
        ),
        migrations.CreateModel(
            name='ISCED_Attainment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kode_level', models.CharField(max_length=1)),
                ('deskripsi_level', models.TextField()),
                ('kode_category', models.CharField(max_length=2)),
                ('deskripsi_category', models.TextField()),
                ('kode_subcategory', models.CharField(max_length=3)),
                ('deskripsi_subcategory', models.TextField()),
                ('dasar_hukum', models.CharField(max_length=120)),
                ('status_data', models.CharField(choices=[('Updated', 'Updated'), ('Depreciated', 'Depreciated')], max_length=11, verbose_name='Status Data')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Klasifikasi Baku Pendidikan',
                'verbose_name_plural': 'Klasifikasi Baku Pendidikan',
            },
        ),
        migrations.CreateModel(
            name='AnggotaKeluarga',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status_anggota', models.CharField(choices=[('Kepala', 'Kepala'), ('Anggota', 'Anggota')], max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keluarga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.keluarga')),
                ('orang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.orang')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Anggota Keluarga',
                'verbose_name_plural': 'Anggota Keluarga',
            },
        ),
    ]
