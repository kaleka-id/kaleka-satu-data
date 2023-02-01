# Generated by Django 4.1.4 on 2023-02-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_alter_fotokegiatan_kegiatan'),
    ]

    operations = [
        migrations.AddField(
            model_name='orang',
            name='keterangan',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orang',
            name='status_data',
            field=models.CharField(choices=[('Updated', 'Updated'), ('Need Confirmation', 'Need Confirmation'), ('Not Valid', 'Not Valid')], default='Need Confirmation', max_length=20),
            preserve_default=False,
        ),
    ]
