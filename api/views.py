from django.shortcuts import render


def index(request):
    data = {
        "title": "Главная Страница"
    }
    return render(request, 'api/index.html', data)


def music(request):
    return render(request, 'api/music.html')


def contact(request):
    data = {
        "title": "Контакты"
    }
    return render(request, 'api/contact.html', data)