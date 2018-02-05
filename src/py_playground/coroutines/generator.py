def print_received():
    received = None
    while True:
        received = yield received
        print("Hello,", received)


if __name__ == '__main__':
    import faker

    fake = faker.Faker()
    generator = print_received()
    next(generator)
    for _ in range(10):
        caller_received = generator.send(fake.name())
        print("Caller received:", caller_received)
