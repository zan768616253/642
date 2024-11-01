from .veggie import Veggie, VeggieType

from app import db

class UnitPriceVeggie(Veggie):
    __mapper_args__ = {'polymorphic_identity': VeggieType.UNIT_PRICE_VEGGIE.value}

    def __init__(self, veg_name, price_per_unit):
        super().__init__(veg_name, VeggieType.UNIT_PRICE_VEGGIE.value, price_per_unit)

    @staticmethod
    def create_unit_price_veggie_with_veggie(veg_name, price_per_unit):
        return UnitPriceVeggie(
            veg_name=veg_name,
            price_per_unit=price_per_unit
        )

