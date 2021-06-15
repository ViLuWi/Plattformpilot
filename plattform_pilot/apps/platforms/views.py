# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from apps.core.filters import nesseccary_suitables
from apps.core.models import Category
from apps.core.views import platform_list
from apps.platforms.models import Platform, Functionality


def platform_detail(request, slug):
    platform = Platform.objects.get(slug=slug)
    category = Category.objects.get(category=platform.category)
    function_count = round(platform.functionality.count() * 10 / category.filter_functions.count(), 2)
    function_count = str(function_count)
    all_functions = category.filter_functions.all().order_by('functionality')
    return render(request, 'platforms/platform-detail.html', {
        'platform': platform,
        'function_count': function_count,
        'all_functions': all_functions,
        'category': category
    })
