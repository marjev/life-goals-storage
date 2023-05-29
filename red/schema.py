import graphene
from graphene_django import DjangoObjectType

from red.models import ComputerScienceEducatorsPost, CseEndeavour


class ComputerScienceEducatorsPostType(DjangoObjectType):
    class Meta:
        model = ComputerScienceEducatorsPost
        fields = ('id', 'stack_exchange_id', 'type', 'text', 'label', 'is_deleted')


class CseEndeavourType(DjangoObjectType):
    class Meta:
        model = CseEndeavour
        fields = ('id', 'value', 'posts')


class Query(graphene.ObjectType):
    all_posts = graphene.List(ComputerScienceEducatorsPostType)
    endeavour_by_value = graphene.Field(CseEndeavourType, value=graphene.String(required=True))

    def resolve_all_posts(root, _):
        return ComputerScienceEducatorsPost.objects.select_related('label').all()

    def resolve_endeavour_by_value(root, _, value):
        try:
            return CseEndeavour.objects.get(value=value)
        except CseEndeavour.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
