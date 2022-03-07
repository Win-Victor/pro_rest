from rest_framework.viewsets import ModelViewSet
from todo.serializers import ProjectsModelSerializer, NotesModelSerializer
from todo.models import Projects, Notes


class ProjectsViewSet(ModelViewSet):
    serializer_class = ProjectsModelSerializer
    queryset = Projects.objects.all()


class NotesViewSet(ModelViewSet):
    serializer_class = NotesModelSerializer
    queryset = Notes.objects.all()
