# Generated by Django 3.2.6 on 2021-09-03 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_whatwedo_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateField(default=datetime.date)),
                ('author', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date', models.DateField(default=datetime.date)),
            ],
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 16, 25, 21, 342297)),
        ),
    ]
