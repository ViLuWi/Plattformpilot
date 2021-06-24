from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'is_checked', 'platform')

admin.site.register(Review, ReviewAdmin)
