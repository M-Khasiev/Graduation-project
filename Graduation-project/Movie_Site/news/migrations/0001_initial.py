# Generated by Django 4.1.7 on 2023-05-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True, verbose_name='Название')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('url_image', models.URLField(default='', verbose_name='Путь к картинке')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
