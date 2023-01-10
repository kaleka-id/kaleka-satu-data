# Generated by Django 4.1.4 on 2023-01-10 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0017_alter_catalog_embed_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('avatar', models.CharField(blank=True, choices=[('/static/images/avatar/brownbear.png', 'Brown Bear'), ('/static/images/avatar/bull.png', 'Bull'), ('/static/images/avatar/camel.png', 'Camel')], max_length=70, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]