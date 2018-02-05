import faker


def print_received():
    received = None
    while True:
        received = yield received
        print("Hello,", received)


def name_generator(times):
    fake = faker.Faker()
    for _ in range(times):
        yield fake.name()


def generate_10_names():
    yield from name_generator(10)


if __name__ == '__main__':
    print_received_generator = print_received()
    next(print_received_generator)
    for name in generate_10_names():
        print_received_generator.send(name)
