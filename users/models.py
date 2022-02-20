from django.contrib.auth.models import AbstractUser
from django.db import models


class ProUser(AbstractUser):
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.DateField(null=True)
    email = models.EmailField(unique=True)
