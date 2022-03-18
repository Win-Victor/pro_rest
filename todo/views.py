from django.views.generic import detail
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from todo.serializers import ProjectsModelSerializer, NotesModelSerializer
from todo.models import Projects, Notes
from rest_framework.pagination import LimitOffsetPagination

from users.models import ProUser

# LIMIT_PROJECT_PAGINATION = 10
# LIMIT_NOTES_PAGINATION = 20
#
#
# class ProjectLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = LIMIT_PROJECT_PAGINATION
#
#
# class NotesLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = LIMIT_NOTES_PAGINATION


class ProjectsViewSet(ModelViewSet):
    # pagination_class = ProjectLimitOffsetPagination
    serializer_class = ProjectsModelSerializer
    queryset = Projects.objects.all()

    # filterset_fields = ['project_name']

    # def get_queryset(self):
    #     queryset = Projects.objects.all()
    #     project_name = self.request.query_params.get('project_name', None)
    #     if project_name:
    #         queryset = queryset.filters(project_name=project_name)
    #     return queryset


class NotesViewSet(ModelViewSet):
    # pagination_class = NotesLimitOffsetPagination
    serializer_class = NotesModelSerializer
    queryset = Notes.objects.all()
    # filterset_fields = ['project']

    # def perform_destroy(self, instance):
    #     instance.is_active = False
    #     instance.save()
