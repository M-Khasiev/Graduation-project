# Generated by Django 4.1.7 on 2023-05-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_movie_imdb_url_movie_kinopoisk_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieshots',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
    ]
