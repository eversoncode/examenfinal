# Generated by Django 2.0.6 on 2021-10-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('pk_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=2)),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefono', models.CharField(blank=True, max_length=8)),
                ('direcciono', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pc',
            fields=[
                ('pk_pc', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=80)),
                ('Ram', models.CharField(max_length=100)),
                ('almacenamiento', models.BigIntegerField()),
                ('modelo', models.CharField(max_length=4)),
            ],
        ),
    ]