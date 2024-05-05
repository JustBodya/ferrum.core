from django.db import models


class Track(models.Model):
    title = models.CharField('Название', max_length=30)
    audio_url = models.URLField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'