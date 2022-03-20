from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from users.serializers import ProUserModelSerializer
from users.models import ProUser


class ProUserViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ProUserModelSerializer
    queryset = ProUser.objects.all()
