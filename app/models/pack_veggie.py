from .veggie import Veggie, VeggieType

from app import db

class PackVeggie(Veggie):
    __mapper_args__ = {'polymorphic_identity': VeggieType.PACK_VEGGIE.value}

    def __init__(self, veg_name, price_per_unit):
        super().__init__(veg_name, VeggieType.PACK_VEGGIE.value, price_per_unit)

    @staticmethod
    def create_pack_veggie_with_veggie(veg_name, price_per_unit):
        return PackVeggie(
            veg_name=veg_name,
            price_per_unit=price_per_unit
        )