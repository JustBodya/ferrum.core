from django.shortcuts import render
from .models import Track


def index(request):
    data = {
        "title": "Главная Страница"
    }
    return render(request, 'api/index.html', data)


def music(request):
    tracks = Track.objects.all()
    return render(request, 'api/music.html', {'tracks': tracks})


def contact(request):
    data = {
        "title": "Контакты"
    }
    return render(request, 'api/contact.html', data)