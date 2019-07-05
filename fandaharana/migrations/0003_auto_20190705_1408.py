# Generated by Django 2.2.3 on 2019-07-05 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fandaharana', '0002_auto_20190705_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name="fanampin'anarana"),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=40, verbose_name='anarana'),
        ),
        migrations.AlterField(
            model_name='public',
            name='date',
            field=models.DateField(verbose_name='daty'),
        ),
        migrations.AlterField(
            model_name='public',
            name='hour_1',
            field=models.TimeField(verbose_name='ora (manomboka)'),
        ),
        migrations.AlterField(
            model_name='public',
            name='hour_2',
            field=models.TimeField(verbose_name='ora (mifarana)'),
        ),
        migrations.AlterField(
            model_name='public',
            name='person_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='public_1', to='fandaharana.Person', verbose_name='mpandray anjara voalohany'),
        ),
        migrations.AlterField(
            model_name='public',
            name='person_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='public_2', to='fandaharana.Person', verbose_name='mpandray anjara faharoa'),
        ),
        migrations.AlterField(
            model_name='public',
            name='place',
            field=models.CharField(max_length=30, verbose_name='toerana'),
        ),
    ]
