import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:'), echo=True)
Base = declarative_base(bind=engine)

session = scoped_session(sessionmaker(bind=engine))

Base.query = session.query_property()


class Greeting(Base):
    __tablename__ = 'greeting'

    id = Column(Integer, primary_key=True)
    greeting = Column(String)
    name = Column(String)


Base.metadata.create_all()
