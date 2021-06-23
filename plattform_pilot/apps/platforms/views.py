# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import render, redirect

from apps.core.filters import nesseccary_suitables
from apps.core.models import Category
from apps.platforms.models import Platform, Functionality
from apps.reviews.forms import ReviewForm


def platform_detail(request, slug):
    platform = Platform.objects.get(slug=slug)
    category = Category.objects.get(category=platform.category)
    function_count = round(platform.functionality.count() * 10 / category.filter_functions.count(), 2)
    function_count = str(function_count)
    all_functions = category.filter_functions.all().order_by('functionality')

    # review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.rating = form.cleaned_data['rating']
            form.save()
            messages.success(request, 'Super! Ihre Bewertung wird von uns geprüft und anschließend freigeschaltet.')
            return redirect('platform:platform_detail', platform.slug)
    else:
        form = ReviewForm()
    return render(request, 'platforms/platform-detail.html', {
        'platform': platform,
        'function_count': function_count,
        'all_functions': all_functions,
        'category': category,
        'form': form
    })
