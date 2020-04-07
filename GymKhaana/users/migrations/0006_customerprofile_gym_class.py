# Generated by Django 2.2.6 on 2020-04-07 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymnasium', '0010_auto_20200407_1415'),
        ('users', '0005_customerprofile_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='gym_class',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='registered_class', to='gymnasium.GymClass'),
            preserve_default=False,
        ),
    ]