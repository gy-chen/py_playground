import faker
from .model import Greeting
from .model import session as session_factory


def init_data(number=1000):
    """Init with random data

    :param number: number of data want to populate
    :return:
    """
    session = session_factory()
    fake = faker.Faker()
    session.add_all([Greeting(name=fake.name(), greeting=fake.word()) for _ in range(number)])
    session.commit()
