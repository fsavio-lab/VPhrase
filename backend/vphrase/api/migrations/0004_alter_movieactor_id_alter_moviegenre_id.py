# Generated by Django 5.0.7 on 2024-07-25 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieactor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='moviegenre',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
