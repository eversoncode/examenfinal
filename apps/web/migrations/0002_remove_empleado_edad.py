# Generated by Django 2.0.6 on 2021-10-07 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='edad',
        ),
    ]
