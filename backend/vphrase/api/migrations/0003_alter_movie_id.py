# Generated by Django 5.0.7 on 2024-07-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
