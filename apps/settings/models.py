from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Общие настройки'