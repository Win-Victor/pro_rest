from users.models import ProUser
from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=64, unique=True)
    users = models.ManyToManyField(ProUser)

    def __str__(self):
        return f'{self.id}, {self.project_name}, {self.users}'


class Notes(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    author = models.ForeignKey(ProUser, on_delete=models.SET_NULL, blank=True, null=True)
    text = models.CharField(max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}, {self.project}, {self.author}, {self.text}, {self.create_at}, {self.updated_at},' \
               f' {self.is_active}'
