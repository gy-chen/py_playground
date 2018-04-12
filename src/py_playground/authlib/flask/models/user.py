from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .base import Base, db


class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column('password', db.String(80))
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_user_id(self):
        return self.id

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    @classmethod
    def get_or_create(cls, profile):
        user = cls.query.filter_by(email=profile.email).first()
        if user:
            return user
        user = cls(email=profile.email, name=profile.name)
        db.session.add(user)
        db.session.commit()
        return user

    def to_dict(self):
        return dict(id=self.id, name=self.name)


class Connect(Base):
    __tablename__ = 'connect'

    id = db.Column(db.Integer, primary_key=True)
    sub = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    token_type = db.Column(db.String)
    access_token = db.Column(db.String(255), nullable=False)
    refresh_token = db.Column(db.String)
    expires_at = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('connects', lazy=True))

    def to_dict(self):
        return dict(
            access_token=self.access_token,
            refresh_token=self.refresh_token,
            token_type=self.token_type,
            expires_at=self.expires_at
        )

    @classmethod
    def create_token(cls, name, token, user):
        conn = cls.query.filter_by(user_id=user.id, name=name).first()
        if not conn:
            conn = cls(user_id=user.id, name=name)

        conn.access_token = token['access_token']
        conn.token_type = token.get('token_type')
        conn.refresh_token = token.get('refresh_token')
        conn.expires_in = token.get('expires_in')
        conn.sub = token['sub']
        db.session.add(conn)
        db.session.commit()
        return conn
