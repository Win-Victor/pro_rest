from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, force_authenticate
from users.models import ProUser
from todo.models import Notes, Projects
from mixer.backend.django import mixer

STATUS_200 = status.HTTP_200_OK


class TestNotesClientAPIMixer(APITestCase):
    def setUp(self) -> None:
        for i in range(10):
            mixer.blend(Notes)
        self.admin = ProUser.objects.create_superuser(username='Super', email='super@local.com', password='Super')

    def test_get_list_1(self):
        self.client.force_login(self.admin)
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 10)


class TestProjectsMixer(APITestCase):
    def setUp(self) -> None:
        for i in range(100):
            mixer.blend(Projects)
        self.admin = ProUser.objects.create_superuser(username='Super', email='super@local.com', password='Super')

    def test_get_list_1(self):
        self.client.force_login(self.admin)
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 100)
