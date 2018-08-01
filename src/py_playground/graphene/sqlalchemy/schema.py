import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .model import Greeting as GreetingModel


class Greeting(SQLAlchemyObjectType):
    class Meta:
        model = GreetingModel
        use_connection = True


class Query(graphene.ObjectType):
    all_greetings = SQLAlchemyConnectionField(Greeting)


schema = graphene.Schema(query=Query)
