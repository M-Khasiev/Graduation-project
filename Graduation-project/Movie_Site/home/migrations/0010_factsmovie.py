# Generated by Django 4.1.7 on 2023-05-20 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_movie_adding_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactsMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Факты о фильме',
                'verbose_name_plural': 'Факты о фильме',
            },
        ),
    ]
