# Generated by Django 3.2.9 on 2022-01-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_url_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AlterField(
            model_name='url',
            name='url_hash',
            field=models.URLField(blank=True, unique=True, verbose_name='Сокращённый URL'),
        ),
    ]