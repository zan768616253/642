import enum
from sqlalchemy import Enum

from app import db


class ItemType(enum.Enum):
    VEGGIE = "VEGGIE"
    PREMADE_BOX = "PREMADE_BOX"


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(100), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'item',
        'polymorphic_on': type
    }

    def __init__(self, type):
        self.type = type
