from django.contrib.auth.models import User
from django.db import models, IntegrityError
from hashlib import md5


domain = 'http://127.0.0.1:8000/'


class Url(models.Model):
    """Модель ссылки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_url = models.URLField(blank=False, verbose_name='Полный URL')
    url_hash = models.URLField(blank=True, verbose_name='Сокращённый URL', unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            hashed = md5(self.full_url.encode()).hexdigest()[:10]
            try:
                self.url_hash = domain + hashed
            except IntegrityError:
                double_hashed = md5(hashed.encode()).hexdigest()[:10]
                self.url_hash = domain + double_hashed
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.full_url

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        unique_together = ['user', 'full_url']
