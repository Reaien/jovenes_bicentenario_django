# Generated by Django 5.0.2 on 2024-07-30 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_region_comuna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comunas', to='web.region'),
        ),
    ]
