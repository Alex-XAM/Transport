from random import choice, randint
from ..Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._trip_counter = 0
        self._speed = 90 # средняя скорость
        # Это вместо ODOMETER_CRITICAL. Поле в классе более гибко, чем константа, т.к. оно наследуется.
        self._mtbf = 40000  # [км]

    def __str__(self):
        return super().__str__() + f' {self._trip_counter} км пробега]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._trip_counter} км пробега'

    @property
    def trip_counter(self):
        return self._trip_counter

    def move(self, distance: int):
        if self._trip_counter > self._mtbf:
            self.functional = choice([True, False, True])
        self._trip_counter += distance if self.functional else randint(0, distance)
