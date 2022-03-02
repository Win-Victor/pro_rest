from rest_framework.viewsets import ModelViewSet
from users.serializers import ProUserModelSerializer
from users.models import ProUser


class ProUserViewSet(ModelViewSet):
    serializer_class = ProUserModelSerializer
    queryset = ProUser.objects.all()
