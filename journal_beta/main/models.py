from django.db import models


class MainPage(models.Model):
    title = models.CharField('Заголовок', max_length=30)
    help_text = models.TextField('Текст бокового меню')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    # def __str__(self):
    #     return 'Главная страница'
