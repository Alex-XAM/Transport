from math import ceil
from random import choice, randint
from ..Vehicle import Vehicle

OPERATING_HOURS_CRITICAL = 1000  # Моточасы двигателя, после которого летательный аппарат ломается


class Helicopter(Vehicle):
    def __init__(self):
        super().__init__()
        self._fuel = 'бензин'
        self._distance_reserve = 1200
        self._hour_counter = 0
        self._speed = 200 # средняя скорость для пересчёта
        self._name = 'вертолёт'

    def __str__(self):
        return super().__str__() + f' {self._hour_counter} часов полёта]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._hour_counter} часов полёта'

    @property
    def hour_counter(self):
        return self._hour_counter

    def move(self, distance: int):
        if self._hour_counter > OPERATING_HOURS_CRITICAL:
            self.functional = choice([True, False, True])
        self._hour_counter += ceil(distance / self._speed) if self.functional else randint(0, ceil(distance / self._speed))
