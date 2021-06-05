from django.urls import path

from .views import *

app_name = 'platform'

urlpatterns = [
    path('', platform_detail, name="platform_detail")
]