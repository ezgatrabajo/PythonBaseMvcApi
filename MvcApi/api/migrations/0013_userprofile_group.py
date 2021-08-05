# Generated by Django 3.2.5 on 2021-08-03 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api', '0012_auto_20210803_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
            preserve_default=False,
        ),
    ]
