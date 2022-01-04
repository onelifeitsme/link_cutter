from django.contrib.auth.models import User
from django.db import models
from hashlib import md5

class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_url = models.URLField(blank=False, verbose_name='Полный URL')
    url_hash = models.URLField(blank=True, verbose_name='Сокращённый URL')

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.full_url






