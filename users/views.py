from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from users.serializers import ProUserModelSerializer, ProUserModelSerializerAdmin
from users.models import ProUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions


class ProUserViewSet(ModelViewSet):
    # permission_classes = [DjangoModelPermissions]
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # serializer_class = ProUserModelSerializer
    queryset = ProUser.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return ProUserModelSerializerAdmin
        return ProUserModelSerializer
