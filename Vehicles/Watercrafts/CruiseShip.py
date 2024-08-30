from .Watercraft import Watercraft


class CruiseShip(Watercraft):
    def __init__(self):
        super().__init__()
        self._fuel = 'дизельное топливо'
        self._distance_reserve = 10000
        self._name = 'круизный лайнер'
        self._speed = 40  # средняя скорость
