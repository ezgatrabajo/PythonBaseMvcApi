# Generated by Django 3.2.5 on 2021-08-02 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20210729_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parametro',
            old_name='valordecimal',
            new_name='valor_decimal',
        ),
        migrations.RenameField(
            model_name='parametro',
            old_name='valorfecha',
            new_name='valor_fecha',
        ),
        migrations.RenameField(
            model_name='parametro',
            old_name='valorinteger',
            new_name='valor_integer',
        ),
        migrations.RenameField(
            model_name='parametro',
            old_name='valortexto',
            new_name='valor_texto',
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=25)),
                ('apellido', models.CharField(blank=True, max_length=25)),
                ('direccion', models.CharField(blank=True, max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=25)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]