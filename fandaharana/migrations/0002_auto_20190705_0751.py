# Generated by Django 2.2.3 on 2019-07-05 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fandaharana', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
