from users.models import ProUser
from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=64, unique=True, verbose_name="Название проекта")
    users = models.ManyToManyField(ProUser, verbose_name="Участники проекта")

    def __str__(self):
        return f'{self.id}, {self.project_name}, {self.users}'


class Notes(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="Проект")
    author = models.ForeignKey(ProUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Создал заметку")
    text = models.CharField(max_length=256, verbose_name="Содержание")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активна (да/нет)")

    def __str__(self):
        return f'{self.id}, {self.project}, {self.author}, {self.text}, {self.create_at}, {self.updated_at},' \
               f' {self.is_active}'
