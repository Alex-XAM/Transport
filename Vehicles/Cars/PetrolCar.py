from .Car import Car


class PetrolCar(Car):
    def __init__(self):
        super().__init__()
        self._fuel = 'бензин'
        self._distance_reserve = 1000
        self._name = 'бензиновый автомобиль'
