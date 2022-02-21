from django.contrib.auth.models import AbstractUser
from django.db import models


class ProUser(AbstractUser):
    username = models.CharField(max_length=64, unique=True, verbose_name='Ник')
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    birthday = models.DateField(null=True, verbose_name='Дата рождения')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')

    def __str__(self):
        return self.id, self.username, self.email
