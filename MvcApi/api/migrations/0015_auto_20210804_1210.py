# Generated by Django 3.2.5 on 2021-08-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_userprofile_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='numero',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='piso',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (7, 'Domingo')]),
        ),
    ]
