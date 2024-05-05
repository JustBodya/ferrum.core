from django.db import models

class FerrumMusic(models.Model):
    title = models.CharField('Название', max_length=30)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Текст')
    data = models.DateField('Дата Публикации')

    def __str__(self):
        return self.title
    
    def  get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'