import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return 'Hello {}'.format(name)


schema = graphene.Schema(query=Query)

if __name__ == '__main__':
    result = schema.execute("{ hello }")
    print(result.data['hello'])
