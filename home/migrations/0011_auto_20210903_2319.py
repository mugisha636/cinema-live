# Generated by Django 3.2.6 on 2021-09-03 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210903_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='genre',
            field=models.CharField(default='Action', max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 23, 19, 24, 536325)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 23, 19, 24, 536325)),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 23, 19, 24, 531327)),
        ),
    ]
