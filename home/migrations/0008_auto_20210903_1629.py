# Generated by Django 3.2.6 on 2021-09-03 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210903_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 3, 16, 29, 10, 184297)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 3, 16, 29, 10, 184297)),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 16, 29, 10, 184297)),
        ),
    ]