from rest_framework.serializers import ModelSerializer
from todo.models import Projects, Notes


class ProjectsModelSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class NotesModelSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
