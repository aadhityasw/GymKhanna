# Generated by Django 2.2.6 on 2019-12-27 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('userAccounts', '0002_auto_20191227_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date', models.DateField()),
            ],
        ),
    ]
