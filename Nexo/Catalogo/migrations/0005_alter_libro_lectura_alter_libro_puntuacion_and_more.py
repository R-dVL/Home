# Generated by Django 4.1 on 2022-11-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0004_auto_20221105_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='lectura',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de lectura'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='puntuacion',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='subgenero',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='puntuacion',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='subgenero',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='visualizacion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de visualización'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='puntuacion',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='subgenero',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='visualizacion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de visualización'),
        ),
    ]
