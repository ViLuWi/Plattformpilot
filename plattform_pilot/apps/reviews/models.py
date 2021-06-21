from django.db import models


class Review(models.Model):
    author = models.CharField(max_length=200)
    content = models.TextField(max_length=1000, blank=True, null=True)
    rating = models.IntegerField(default=5)
    is_checked = models.BooleanField(default=False)
