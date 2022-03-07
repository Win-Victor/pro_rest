from users.models import ProUser
from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=64, unique=True)
    users = models.ManyToManyField(ProUser)


class Notes(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    author = models.ForeignKey(ProUser, on_delete=models.SET_NULL, blank=True, null=True)
    text = models.CharField(max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
