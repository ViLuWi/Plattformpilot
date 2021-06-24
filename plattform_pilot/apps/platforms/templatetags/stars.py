from django import template

register = template.Library()

def stars(value):
    if value == 1:
        return '&#9733;'
    elif value == 2:
        return '&#9733;&#9733;'
    elif value == 3:
        return '&#9733;&#9733;&#9733;'
    elif value == 4:
        return '&#9733;&#9733;&#9733;&#9733;'
    elif value == 5:
        return '&#9733;&#9733;&#9733;&#9733;&#9733;'

def stars_half(value):
    if value >= 1 and value < 1.5:
        return '&#9733;'
    elif value >= 1.5 and value < 2:
        return '&#9733;&#9734;'
    elif value >= 2 and value < 2.5:
        return '&#9733;&#9733;'
    elif value >= 2.5 and value < 3:
        return '&#9733;&#9733;&#9734;'
    elif value >= 3 and value < 3.5:
        return '&#9733;&#9733;&#9733;'
    elif value >= 3.5 and value < 4:
        return '&#9733;&#9733;&#9733;&#9734;'
    elif value >= 4 and value < 4.5:
        return '&#9733;&#9733;&#9733;&#9733;'
    elif value >= 4.5 and value < 5:
        return '&#9733;&#9733;&#9733;&#9734;'
    elif value >= 5:
        return '&#9733;&#9733;&#9733;&#9733;&#9733;'

register.filter('stars', stars)
register.filter('stars_half', stars_half)