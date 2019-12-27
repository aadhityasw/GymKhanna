# Generated by Django 2.2.6 on 2019-12-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymnasium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Equipment Type',
                'verbose_name_plural': 'Equipment Types',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(max_length=4)),
                ('timings', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.AlterModelOptions(
            name='amc',
            options={'verbose_name': 'AMC', 'verbose_name_plural': 'AMC'},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': 'Equipment', 'verbose_name_plural': 'Equipments'},
        ),
    ]
