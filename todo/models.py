from users.models import ProUser
from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=64, unique=True)
    users = models.ManyToManyField(ProUser)


class Notes(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    users = models.ManyToManyField(ProUser)
    text = models.CharField(max_length=256)
