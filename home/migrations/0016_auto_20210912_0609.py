# Generated by Django 3.2.7 on 2021-09-12 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210903_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 6, 9, 29, 434727)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 6, 9, 29, 434727)),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 6, 9, 29, 414595)),
        ),
    ]