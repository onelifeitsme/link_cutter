# Generated by Django 3.2.9 on 2022-01-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_url_full_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='url_hash',
            field=models.URLField(blank=True),
        ),
    ]
