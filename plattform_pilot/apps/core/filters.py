import django_filters
from django import forms

from apps.core.models import Category
from apps.platforms.models import Functionality, Platform, Suitable


def nesseccary_functionalities(slug):
    # select nesseccary functionalities
    category = Category.objects.get(slug=slug)
    categoryNesseccary = list(category.filter_functions.values('functionality'))
    filter_funcs = list(Functionality.objects.values_list('functionality', flat=True))

    for count, x in enumerate(categoryNesseccary):
        if x['functionality'] in filter_funcs:
            filter_funcs.remove(x['functionality'])
    return filter_funcs

def nesseccary_suitables():
    # select nesseccary functionalities
    platforms = Platform.objects.all()
    suit_list = []
    filter_funcs = list(platforms.values('suitable_for'))

    for count, x in enumerate(filter_funcs):
        if x['suitable_for'] not in suit_list:
            suit_list.append(x['suitable_for'])
    return suit_list


class PlatformFilter(django_filters.FilterSet, object):

    # filters
    nesseccary = Functionality.objects.all().order_by('functionality')
    is_free = django_filters.BooleanFilter(field_name='is_free', label='Kostenlose Variante',
                                           widget=forms.CheckboxInput)
    suitable_for = django_filters.ModelMultipleChoiceFilter(field_name='suitable_for', conjoined=True,
                                                            queryset=Suitable.objects.all(), widget=forms.CheckboxSelectMultiple)
    price = django_filters.RangeFilter(field_name='pricing', label='Preisspanne')
    funktion = django_filters.ModelMultipleChoiceFilter(field_name='functionality', conjoined=True, queryset=nesseccary,
                                                        widget=forms.CheckboxSelectMultiple(
                                                            attrs={'class': 'function__list'}))
