from .Watercraft import Watercraft


class SpeedBoat(Watercraft):
    def __init__(self):
        super().__init__()
        self._fuel = 'бензин'
        self._distance_reserve = 500
        self._name = 'катер'
        self._speed = 60  # средняя скорость
