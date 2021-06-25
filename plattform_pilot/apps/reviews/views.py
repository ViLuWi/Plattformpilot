from django.shortcuts import render
from django.core.paginator import Paginator

from apps.platforms.models import Platform
from apps.reviews.models import Review


def reviews(request, slug):
    platform = Platform.objects.get(slug=slug)
    reviews = Review.objects.filter(platform=platform, is_checked=True)
    sort_date = request.GET.get('date')
    sort_rating = request.GET.get('rating')
    if sort_rating is not None and sort_rating is not '':
        reviews = reviews.order_by(sort_rating)
    if sort_date is not None and sort_date is not '':
        reviews = reviews.order_by(sort_date)
    if sort_date is not None and sort_rating is not None:
        reviews = reviews.order_by(sort_date, sort_rating)

    # pagination
    paginator = Paginator(reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reviews/reviews.html', {
        'reviews': reviews,
        'platform': platform,
        'page_obj': page_obj
    })
