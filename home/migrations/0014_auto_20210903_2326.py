# Generated by Django 3.2.6 on 2021-09-03 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210903_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 23, 26, 43, 556551)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 23, 26, 43, 556551)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 23, 26, 43, 556551)),
        ),
    ]
