import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .model import Greeting as GreetingModel


class Greeting(SQLAlchemyObjectType):
    class Meta:
        model = GreetingModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_greetings = SQLAlchemyConnectionField(Greeting)


schema = graphene.Schema(query=Query)
