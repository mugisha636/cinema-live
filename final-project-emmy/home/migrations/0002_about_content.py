# Generated by Django 3.2.6 on 2021-08-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
