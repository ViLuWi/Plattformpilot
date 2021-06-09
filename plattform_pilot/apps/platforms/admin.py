# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'is_free')

admin.site.register(Platform, PlatformAdmin)
admin.site.register(Functionality)
admin.site.register(Suitable)
