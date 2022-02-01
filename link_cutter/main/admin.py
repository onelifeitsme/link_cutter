from django.contrib import admin

# Register your models here.
from .models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = ('full_url', 'user')
    search_fields = ('full_url', 'user')


admin.site.register(Url)
