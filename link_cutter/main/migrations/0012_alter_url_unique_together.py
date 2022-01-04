# Generated by Django 3.2.9 on 2022-01-04 19:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_alter_url_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='url',
            unique_together={('user', 'full_url')},
        ),
    ]
