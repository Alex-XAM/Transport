from .Car import Car


class ElectroCar(Car):
    def __init__(self):
        super().__init__()
        self._fuel = 'электричество'
        self._distance_reserve = 900
        self._name = 'электромобиль'
