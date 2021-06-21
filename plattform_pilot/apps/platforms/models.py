# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField

class Functionality(models.Model):
    functionality = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.functionality}'


class Suitable(models.Model):
    suitable_for = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.suitable_for}'


class Platform(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    slug = models.SlugField(max_length=200, default=uuid.uuid1, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='platforms/thumbnails')
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    suitable_for = models.ManyToManyField(Suitable, verbose_name='Geeignet für')
    suitable_for_text = models.TextField(max_length=1000, default='', verbose_name='Geeignet für Text', blank=True,
                                         null=True)
    is_free = models.BooleanField(default=False, verbose_name='Kostenlose variante')
    pricing = models.DecimalField(verbose_name='Startpreis', decimal_places=2, max_digits=5)
    pricing_note = models.CharField(max_length=200, verbose_name='Startpreis für')
    pricing_text = models.TextField(blank=True, null=True)
    price_rating = models.CharField(max_length=10, blank=True, null=True)
    functionality = models.ManyToManyField(Functionality, max_length=200, verbose_name='Funktionalitäten')
    image_detail = models.ImageField(upload_to='platforms/images', blank=True, null=True)
    short_description = models.TextField(max_length=50000, blank=True, null=True)
    who_use_it = models.TextField(max_length=50000, blank=True, null=True)
    when_to_use = models.TextField(max_length=50000, blank=True, null=True)
    link = models.CharField(max_length=50000)
    tutorial = models.TextField(max_length=50000, blank=True, null=True)
    tutorial_video = EmbedVideoField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    design_rating = models.CharField(max_length=10, blank=True, null=True)
    tested = models.BooleanField(default=False)
    test_report = models.TextField(max_length=50000, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Plattformen'

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Platform, self).save(*args, **kwargs)

