# Generated by Django 2.2 on 2019-08-08 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20190808_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='descripcion',
        ),
    ]
