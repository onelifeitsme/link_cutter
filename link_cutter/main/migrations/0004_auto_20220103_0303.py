# Generated by Django 3.2.9 on 2022-01-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_url_url_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='full_url',
            field=models.URLField(verbose_name='Полный URL'),
        ),
        migrations.AlterField(
            model_name='url',
            name='url_hash',
            field=models.URLField(blank=True, verbose_name='Сокращённый URL'),
        ),
    ]
