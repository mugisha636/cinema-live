# Generated by Django 3.2.7 on 2021-09-14 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20210913_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 14, 9, 11, 28, 441329)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 14, 9, 11, 28, 441329)),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 14, 9, 11, 28, 427674)),
        ),
    ]
