# Generated by Django 5.0.1 on 2024-01-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='textoNoticia1',
            field=models.CharField(max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='textoNoticia2',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
    ]
