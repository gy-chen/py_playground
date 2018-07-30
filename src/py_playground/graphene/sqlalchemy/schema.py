import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .model import session, Greeting as GreetingModel


class Greeting(SQLAlchemyObjectType):
    class Meta:
        model = GreetingModel
        interfaces = (relay.Node,)


class GreetingConnection(relay.Connection):
    class Meta:
        node = Greeting


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_greetings = SQLAlchemyConnectionField(GreetingConnection)


schema = graphene.Schema(query=Query)
