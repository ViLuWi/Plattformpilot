# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'is_free')
    # summernote_fields = ('pricing_text', 'short_description', 'when_to_use', 'who_to_use', 'tutorial', 'test_report')


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Functionality)
admin.site.register(Suitable)
