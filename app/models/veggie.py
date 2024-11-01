import enum
from sqlalchemy import Enum

from .item import Item, ItemType

from app import db


class VeggieType(enum.Enum):
    WEIGHTED_VEGGIE = "WEIGHTED_VEGGIE"
    PACK_VEGGIE = "PACK_VEGGIE"
    UNIT_PRICE_VEGGIE = "UNIT_PRICE_VEGGIE"

class Veggie(Item):
    __tablename__ = 'veggies'

    veggie_id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    veg_name = db.Column(db.String(100), nullable=False)
    subtype = db.Column(db.String(100), nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=100)

    __mapper_args__ = {
        'polymorphic_identity': ItemType.VEGGIE.value,
        'polymorphic_on': subtype
    }

    def __init__(self, veg_name, subtype, price_per_unit):
        super().__init__(ItemType.VEGGIE.value)
        self.veg_name = veg_name
        self.subtype = subtype
        self.price_per_unit = price_per_unit
