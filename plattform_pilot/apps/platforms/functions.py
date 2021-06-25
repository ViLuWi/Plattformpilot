from apps.platforms.models import Platform
from apps.reviews.models import Review

# calculate average rating
def calc_rating(id):
    platform = Platform.objects.get(id=id)
    reviews = Review.objects.all().exclude(is_checked=False)
    counter = 0
    iterations = 0
    for count, i in enumerate(reviews):
        if i.platform == platform:
            counter += i.rating
            iterations += 1

    if iterations > 0:
        return counter/iterations
    else:
        return 0
