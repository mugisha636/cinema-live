# Generated by Django 3.2.7 on 2021-09-13 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20210913_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 13, 16, 31, 31, 996922)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 13, 16, 31, 32, 1917)),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 13, 16, 31, 31, 991906)),
        ),
    ]
