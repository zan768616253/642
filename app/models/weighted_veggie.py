from .veggie import Veggie, VeggieType

class WeightedVeggie(Veggie):
    __mapper_args__ = {
        'polymorphic_identity': VeggieType.WEIGHTED_VEGGIE.value
    }

    def __init__(self, veg_name, price_per_unit):
        super().__init__(veg_name, VeggieType.WEIGHTED_VEGGIE.value, price_per_unit)

    @staticmethod
    def create_weighted_veggie_with_veggie(veg_name, price_per_unit):
        return WeightedVeggie(
            veg_name=veg_name,
            price_per_unit=price_per_unit
        )
