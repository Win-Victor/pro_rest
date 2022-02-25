from django.conf import settings
from django.core.management.base import BaseCommand
from users.models import ProUser
from django.contrib.auth.models import User
import json, os

JSON_PATH = 'users/json'


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('users')
        ProUser.objects.all().delete()
        for user in users:
            ProUser.objects.create(**user)


        admin_user = ProUser.objects.create_superuser(username='Jimmy', email='django@geekshop.local', password='rest365')
