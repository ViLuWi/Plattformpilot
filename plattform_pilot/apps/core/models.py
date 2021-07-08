# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

from tinymce.models import HTMLField
from apps.platforms.models import Functionality, Suitable


class Category(models.Model):
    category = models.CharField(max_length=200)
    description = HTMLField(max_length=5000, default='')
    slug = models.SlugField(blank=True, null=True)
    filter_functions = models.ManyToManyField(Functionality, verbose_name='Filtern nach')
    related_category = models.ManyToManyField('self', related_name='related_category', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.category}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)
