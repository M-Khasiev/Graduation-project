# Generated by Django 4.1.7 on 2023-05-31 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_movieshots_cms_css'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='age_rating',
            field=models.IntegerField(choices=[(0, '0+'), (6, '6+'), (12, '12+'), (16, '16+'), (18, '18+')], default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='eng_title',
            field=models.CharField(default='', max_length=100, verbose_name='Название на английском'),
        ),
    ]
