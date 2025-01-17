# Generated by Django 5.0.7 on 2024-07-25 14:48

import api.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField(choices=api.utils.years_range, verbose_name='year')),
                ('description', models.TextField(max_length=1024)),
                ('director', models.CharField(max_length=255)),
                ('votes', models.IntegerField()),
                ('runtime', models.SmallIntegerField()),
                ('grossing_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stars', models.ManyToManyField(to='api.movieactor')),
                ('genre', models.ManyToManyField(to='api.moviegenre')),
            ],
        ),
    ]
