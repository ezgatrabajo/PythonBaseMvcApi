# Generated by Django 3.2.5 on 2021-08-02 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_horario_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado'), (7, 'Domingo')], max_length=1),
        ),
    ]