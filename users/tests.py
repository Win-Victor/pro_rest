from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, force_authenticate

from users.models import ProUser
from users.views import ProUserViewSet
from mixer.backend.django import mixer

STATUS_200 = status.HTTP_200_OK


class TestProUserAPI(TestCase):

    def test_get_list_1(self):
        factory = APIRequestFactory()
        request = factory.get('api/users/')
        view = ProUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 0)

    def test_get_list_1_1(self):
        factory = APIRequestFactory()
        user = ProUser.objects.create_superuser(username='Super', email='super@local.com', password='Super')
        request = factory.get('api/users/')
        force_authenticate(request, user)
        view = ProUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 1)

    def test_get_list_2(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = ProUserViewSet.as_view({'get': 'list'})
        ProUser.objects.create(username='User', email='fgfgfg@local.com', password='DRF')
        response = view(request)
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 1)

    def test_get_list_3(self):
        client = APIClient()
        ProUser.objects.create(username='User', email='fgfgfg@local.com', password='DRF')
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 1)


class TestUserClientAPI(APITestCase):
    def test_get_list_1(self):
        ProUser.objects.create(username='User', email='fgfgfg@local.com', password='DRF')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 1)

    def test_get_list_2(self):
        ProUser.objects.create_superuser(username='Super', email='super@local.com', password='Super')
        ProUser.objects.create(username='User', email='fgfgfg@local.com', password='DRF')
        self.client.login(username='Super', password='Super')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 2)  # user and superuser in 1 model


class TestAdminUserClientAPI(APITestCase):
    def setUp(self) -> None:
        ProUser.objects.create(username='User', email='fgfgfg@local.com', password='DRF')
        self.admin = ProUser.objects.create_superuser(username='Super', email='super@local.com', password='Super')

    def test_get_list_1(self):
        self.client.force_login(self.admin)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 2)

    def test_get_list_2(self):
        self.client.login(username='Super', password='Super')
        # self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 2)  # user and superuser in 1 model


class TestUserClientAPIMixer(APITestCase):
    def setUp(self) -> None:
        for i in range(9):
            mixer.blend(ProUser)
        self.admin = ProUser.objects.create_superuser(username='Super', email='super@local.com', password='Super')

    def test_get_list_1(self):
        self.client.force_login(self.admin)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, STATUS_200)
        self.assertEqual(len(response.data), 10)
