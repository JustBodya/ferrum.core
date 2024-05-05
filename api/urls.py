from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('music', views.music, name='music'),
    path('contact', views.contact, name='contact'),
]