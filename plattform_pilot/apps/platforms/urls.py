from django.urls import path

from .views import *

app_name = 'platform'

urlpatterns = [
    path('<slug>', platform_detail, name="platform_detail")
]