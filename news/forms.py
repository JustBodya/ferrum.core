from .models import FerrumMusic
from django.forms import ModelForm, TextInput, DateInput, Textarea


class FerrumMusicForm(ModelForm):
    class Meta:
        model = FerrumMusic
        fields = ['title', 'anons', 'text', 'data']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс новости'
            }),
            "data": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости'
            })
            
        }