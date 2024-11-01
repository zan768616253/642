import enum
from sqlalchemy import Enum

from .item import Item, ItemType

from app import db

class BoxSize(enum.Enum):
    L = "L"
    S = "S"

class PremadeBox(Item):
    __tablename__ = 'premade_boxes'

    id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    box_size = db.Column(Enum(BoxSize), nullable=False)
    prize = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=100)

    __mapper_args__ = {'polymorphic_identity': ItemType.PREMADE_BOX.value}

    def __init__(self, box_size, prize):
        super().__init__(ItemType.PREMADE_BOX.value)
        self.box_size = box_size
        self.prize = prize