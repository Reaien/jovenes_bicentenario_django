# Generated by Django 5.0.1 on 2024-01-31 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_envivos_alter_regiones_correodelegado'),
    ]

    operations = [
        migrations.AddField(
            model_name='regiones',
            name='votos',
            field=models.IntegerField(default=0),
        ),
    ]
