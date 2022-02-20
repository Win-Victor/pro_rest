from rest_framework.viewsets import ModelViewSet
from users.serializers import UserModelSerializer
from users.models import Users


class UsersViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = Users.objects.all()
