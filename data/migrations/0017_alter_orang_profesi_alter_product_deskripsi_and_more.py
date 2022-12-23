# Generated by Django 4.1.4 on 2022-12-23 06:46

import data.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_alter_product_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orang',
            name='profesi',
            field=models.ManyToManyField(blank=True, to='data.profesi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='deskripsi',
            field=models.ForeignKey(help_text='Gunakan tabel <a target="blank" href="/dict/testing-artikel/">Testing Artikel</a> sebagai referensi untuk mengisi bagian ini', on_delete=django.db.models.deletion.CASCADE, to='data.testing'),
        ),
        migrations.AlterField(
            model_name='product',
            name='foto',
            field=models.FileField(blank=True, help_text='Gunakan file ekstensi .jpg, .jpeg atau .png', null=True, upload_to='testing/', validators=[data.validators.file_image]),
        ),
        migrations.AlterField(
            model_name='product',
            name='toko',
            field=models.ManyToManyField(blank=True, to='data.shop'),
        ),
    ]
