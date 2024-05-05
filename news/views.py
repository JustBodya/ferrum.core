from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import FerrumMusic
from .forms import FerrumMusicForm


def news_home(request):
    news = FerrumMusic.objects.order_by('-data')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = FerrumMusic
    template_name = 'news/details_view.html'
    context_object_name = 'ferrum'


class NewsUpdateView(UpdateView):
    model = FerrumMusic
    template_name = 'news/create.html'

    form_class = FerrumMusicForm


class NewsDeleteView(DeleteView):
    model = FerrumMusic
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = FerrumMusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной!'

    form = FerrumMusicForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)