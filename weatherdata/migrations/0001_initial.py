# Generated by Django 4.2.7 on 2023-11-21 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeaAreaForecastMetIe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('until_time', models.CharField(max_length=250)),
                ('issued_time', models.CharField(max_length=250)),
                ('gale_status', models.CharField(max_length=10)),
                ('small_craft_status', models.CharField(max_length=10)),
                ('met_sit_head', models.TextField()),
                ('met_sit_time', models.CharField(max_length=250)),
                ('met_sit_text', models.TextField()),
                ('outlook_time', models.CharField(max_length=250)),
                ('outlook_head', models.TextField()),
                ('outlook_text', models.TextField()),
                ('swell_status', models.CharField(max_length=210)),
                ('area1', models.TextField(blank=True, null=True)),
                ('wind1', models.TextField(blank=True, null=True)),
                ('weather1', models.TextField(blank=True, null=True)),
                ('visibility1', models.TextField(blank=True, null=True)),
                ('area2', models.TextField(blank=True, null=True)),
                ('wind2', models.TextField(blank=True, null=True)),
                ('weather2', models.TextField(blank=True, null=True)),
                ('visibility2', models.TextField(blank=True, null=True)),
                ('area3', models.TextField(blank=True, null=True)),
                ('wind3', models.TextField(blank=True, null=True)),
                ('weather3', models.TextField(blank=True, null=True)),
                ('visibility3', models.TextField(blank=True, null=True)),
                ('area4', models.TextField(blank=True, null=True)),
                ('wind4', models.TextField(blank=True, null=True)),
                ('weather4', models.TextField(blank=True, null=True)),
                ('visibility4', models.TextField(blank=True, null=True)),
                ('area5', models.TextField(blank=True, null=True)),
                ('wind5', models.TextField(blank=True, null=True)),
                ('weather5', models.TextField(blank=True, null=True)),
                ('visibility5', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'source formats',
            },
        ),
        migrations.CreateModel(
            name='WeatherRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'weather records',
            },
        ),
        migrations.CreateModel(
            name='SourceURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('url', models.CharField(max_length=250)),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weatherdata.sourceformat')),
            ],
            options={
                'verbose_name_plural': 'source urls',
            },
        ),
    ]
