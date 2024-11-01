import enum
from sqlalchemy import Enum

from app import db

class PersonType(enum.Enum):
    STAFF = "STAFF"
    CUSTOMER = "CUSTOMER"


class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(100), nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'person'}

    def __init__(self, first_name, last_name, username, password, type):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.type = type
