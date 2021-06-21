from collections import Counter
import time

from django.db.models import Count
from django.shortcuts import render, redirect

from urllib.parse import unquote

from django.urls import reverse

from .models import Category
from .filters import *
from ..platforms.models import Platform


def index(request):
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories
    })


def platform_list(request, slug):
    category = Category.objects.get(slug=slug)
    platforms = Platform.objects.filter(category=category).order_by('-is_featured')
    accuracy = []
    filter_interations = 0
    # calaculate filter iterations for function, suitable
    for i in request.GET.getlist('funktion'):
        filter_interations += 1

    for i in request.GET.getlist('suitable_for'):
        filter_interations += 1

    # ordering query
    sort_by = request.GET.get('sort_by')
    if sort_by is not None and sort_by is not '':
        platforms = platforms.order_by('-is_featured', sort_by)

    # filter query
    unnesseccary = nesseccary_functionalities(slug)
    # suitable_nesseccary = nesseccary_suitables()
    f = PlatformFilter(request.GET, queryset=platforms)
    related_platforms = platforms

    suit_list = []
    # add values to suitable_list for 100% accuracy
    for v in f.qs.all().values('suitable_for'):
        if v['suitable_for'] not in suit_list:
            suit_list.append(v['suitable_for'])
    for x in f.qs.all():
        for y in Platform.objects.get(name=x).suitable_for.all():
            if y.id not in suit_list:
                suit_list.append(y.id)

    # remove doubled platforms form f.qs and related_platforms
    f_values = [d['id'] for d in list(f.qs.all().values('id'))]
    rel_values = [d['id'] for d in list(related_platforms.values('id'))]

    for i in list(rel_values):
        if i in f_values:
            related_platforms = related_platforms.exclude(id=i)
        else:
            platform = Platform.objects.get(id=i)
            f_list = []
            noo = 0
            filter_interations = 0
            for x in platform.functionality.all():
                f_list.append(int(x.id))

            # add all suitables to list
            for x in platform.suitable_for.all():
                suit_list.append(int(x.id))

            # iterate through lists
            for count, x in enumerate(request.GET.getlist('funktion'), start=1):
                filter_interations += 1
                if int(x) not in f_list:
                    noo += 1

            # check suitable for values (y = checked values)
            for count, y in enumerate(request.GET.getlist('suitable_for'), start=1):
                filter_interations += 1
                if int(y) not in suit_list:
                    noo += 1

            if f.data.get('is_free') is None and platform.is_free or f.data.get('is_free') is not platform.is_free:
                noo += 1
                filter_interations += 1
            print(noo, filter_interations)
            accuracy.append({'id': platform.id, 'accuracy': int((1 - (noo / filter_interations)) * 100)})

    # check if category is active
    if category.is_active:
        return render(request, 'core/platform-list.html', {
            'category': category,
            'filter': f,
            'unnesseccary': unnesseccary,
            'suitable_list': suit_list,
            'related_platforms': related_platforms,
            'accurary': accuracy,
            'sort_by': sort_by
        })
    else:
        return render(request, 'error/category-inactive.html')
