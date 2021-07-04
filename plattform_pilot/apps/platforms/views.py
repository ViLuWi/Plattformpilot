# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import render, redirect

from apps.core.filters import nesseccary_suitables
from apps.core.models import Category
from apps.platforms.functions import calc_rating
from apps.platforms.models import Platform, Functionality
from apps.reviews.forms import ReviewForm
from apps.reviews.models import Review


def all_plattforms(request):
    pass


def platform_detail(request, slug):
    platform = Platform.objects.get(slug=slug)
    category = Category.objects.get(category=platform.category)
    function_count = round(platform.functionality.count() * 10 / category.filter_functions.count(), 2)
    function_count = str(function_count)
    all_functions = category.filter_functions.all().order_by('functionality')

    # review
    reviews = Review.objects.filter(platform=platform, is_checked=True).order_by('-created_at', '-rating')
    av_rating = calc_rating(platform.id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['platform'].id)
            #  check if platform is correct
            if form.cleaned_data['platform'].id == platform.id:
                form.save(commit=False)
                form.rating = int(request.POST['rating'])
                form.platform = form.cleaned_data['platform']
                form.save()
                messages.success(request, 'Super! Ihre Bewertung wird von uns geprüft und anschließend freigeschaltet.')
                return redirect('platform:platform_detail', platform.slug)
            else:
                messages.error(request, 'Uups, etwas stimmt nicht. Versuche es nochmal!')
        else:
            messages.error(request, 'Sieht so aus als fehlt hier etwas.. Hast du den Autor und eine Sterne-Bewertung angegeben?')
    else:
        form = ReviewForm()
    return render(request, 'platforms/platform-detail.html', {
        'platform': platform,
        'function_count': function_count,
        'all_functions': all_functions,
        'category': category,
        'form': form,
        'reviews': reviews,
        'av_rating': av_rating,
    })
