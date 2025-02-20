# Generated by Django 5.0.2 on 2024-09-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_rename_imagenencabezado_noticia_imagenpreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='comuna',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='nombre_bailarin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='nombre_bailarina',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='rut_bailarin',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='rut_bailarina',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='telefono_bailarin',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='telefono_bailarina',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
