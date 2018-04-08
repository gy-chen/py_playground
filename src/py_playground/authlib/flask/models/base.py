from flask_sqlalchemy import SQLAlchemy

# initialize using db.init_app later
db = SQLAlchemy()


class Base(db.Model):
    # see http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/api.html?highlight=__abstract__
    __abstract__ = True
