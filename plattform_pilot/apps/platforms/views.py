from django.shortcuts import render


def platform_detail(request):
    return render(request, 'platforms/platform-detail.html', {})
