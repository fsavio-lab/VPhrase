# Generated by Django 5.0.7 on 2024-07-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_movie_description_remove_movie_directors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='runtime',
        ),
    ]
