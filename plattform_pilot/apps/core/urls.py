from django.urls import path

from .views import *

app_name = 'core'


urlpatterns = [
    path('', index, name="index"),
    path('<str:slug>', platform_list, name="platform_list"),
    path('kategorien/alle', all_categories, name="all_categories"),
    path('webseite/datenschutz', terms, name="terms"),
    path('webseite/cookies', cookies, name="cookies"),
]