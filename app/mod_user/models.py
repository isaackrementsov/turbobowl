from app import db
from sqlalchemy.orm import relationship
from app.models import Base


class User(Base):

    DEFAULT_AVATAR = 'default.png'

    __tablename__ = 'user'

    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

    email = db.Column(db.String(128), nullable=False, unique=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    avatar = db.Column(db.String(256), nullable=False, default=DEFAULT_AVATAR)

    @staticmethod
    def find_by_email_or_username(identifer):
        return User.query.filter(db.or_(User.username == identifer, User.email == identifer)).first()

    @staticmethod
    def matches_id(id):
        return User.query.get(id) is not None


class School(Base):

    __tablename__ = 'school'

    name = db.Column(db.String(256), nullable=False, unique=True)
    town = db.Column(db.String(192), nullable=False)
    state = db.Column(db.String(128), nullable=False)
    users = relationship('User')
