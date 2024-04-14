from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length = 50, verbose_name='Имя')
    last_name = models.CharField(max_length = 100, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='День рождения')
    phone = models.CharField(max_length = 15, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Почта')
    comments = models.TextField(blank=True, verbose_name='Комментарии')

class Master(models.Model):
    first_name = models.CharField(max_length = 50, verbose_name='Имя')
    last_name = models.CharField(max_length = 100, verbose_name='Фамилия')
    phone = models.CharField(max_length = 15, verbose_name='Телефон')
    name_service = models.CharField(max_length = 100, verbose_name='Название услуги')


     
