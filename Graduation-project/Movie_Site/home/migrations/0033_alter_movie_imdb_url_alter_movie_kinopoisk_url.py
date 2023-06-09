# Generated by Django 4.2.2 on 2023-07-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_movie_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_url',
            field=models.URLField(default='', verbose_name='URL IMDb'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='kinopoisk_url',
            field=models.URLField(default='', verbose_name='URL Кинопоиск'),
        ),
    ]
