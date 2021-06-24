from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'content', 'rating', 'platform']
        exclude = ['is_checked', ]
