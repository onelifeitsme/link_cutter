# Generated by Django 3.2.9 on 2022-01-03 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_url_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url_hash',
            field=models.URLField(blank=True, unique=True, verbose_name='Сокращённый URL'),
        ),
        migrations.AlterField(
            model_name='url',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
