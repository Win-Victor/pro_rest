import graphene
from graphene_django import DjangoObjectType
from todo.models import Notes, Projects
from users.models import ProUser


class UserType(DjangoObjectType):
    class Meta:
        model = ProUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Projects
        fields = '__all__'


class NotesType(DjangoObjectType):
    class Meta:
        model = Notes
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return ProUser.objects.all()

    user_by_id = graphene.Field(UserType, pk=graphene.Int(required=True))

    def resolve_user_by_id(root, info, pk):
        try:
            return ProUser.objects.get(pk=pk)
        except ProUser.DoesNotExist:
            return None

    user_by_name = graphene.List(UserType, name=graphene.String(required=False))

    def resolve_user_by_name(root, info, name=None):
        users = ProUser.objects.all()
        if name:
            users = ProUser.objects.filter(username=name)
        return users

    all_notes = graphene.List(NotesType)

    def resolve_all_notes(root, info):
        return Notes.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Projects.objects.all()


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday = graphene.Date(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, first_name, last_name, birthday, email):
        user = ProUser(username=username, first_name=first_name, last_name=last_name, birthday=birthday, email=email)
        user.save()
        return cls(user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String(required=False)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        birthday = graphene.Date(required=False)
        email = graphene.String(required=False)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id, username=None, first_name=None, last_name=None, birthday=None, email=None):
        user = ProUser.objects.get(pk=id)
        if username:
            user.username = username
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if birthday:
            user.birthday = birthday
        if email:
            user.email = email
            user.save()
        return cls(user)


class Mutations(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
