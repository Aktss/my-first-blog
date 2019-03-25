from django.shortcuts import render


def landing(request):
    name = "Ky"
    return render(request, 'landing/landing.html', locals())