from twisted.internet.protocol import Protocol, Factory


class Echo(Protocol):

    def __init__(self, factory):
        # The factory is used to share state that exists beyond the lifetime of any given connection
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "Welcome! There are currently {} open connections.\n".format(self.factory.numProtocols).encode('utf8'))

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(Factory):

    numProtocols = 0

    def buildProtocol(self, addr):
        return Echo(self)


if __name__ == '__main__':
    from twisted.internet.endpoints import TCP4ServerEndpoint
    from twisted.internet import reactor
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(EchoFactory())
    reactor.run()