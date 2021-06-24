from datetime import datetime

from django.db import models

from apps.platforms.models import Platform


class Review(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=200)
    content = models.TextField(max_length=1000, blank=True, null=True)
    rating = models.IntegerField(default=5)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, null=True)