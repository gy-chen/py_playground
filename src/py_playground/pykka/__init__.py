import pykka


class Greeter(pykka.ThreadingActor):
    def on_receive(self, message):
        print('Hi there!')
