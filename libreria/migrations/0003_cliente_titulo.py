# Generated by Django 3.2.8 on 2023-08-19 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_auto_20230818_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='titulo',
            field=models.CharField(default='Titulo', max_length=100, verbose_name='Titulo'),
        ),
    ]
