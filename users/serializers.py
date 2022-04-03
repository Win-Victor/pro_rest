from rest_framework.serializers import ModelSerializer
from users.models import ProUser


class ProUserModelSerializer(ModelSerializer):
    class Meta:
        model = ProUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ProUserModelSerializerAdmin(ModelSerializer):
    class Meta:
        model = ProUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']
