# Generated by Django 2.2.1 on 2019-05-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_remove_page_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
