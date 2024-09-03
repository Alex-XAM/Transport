from math import ceil
from ..Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._trip_counter = 0
        self._speed = 90 # [км/ч] средняя скорость
        self._mtbf = 40000  # [км] пробег, после которого ТС ломается

    def __str__(self):
        return super().__str__() + f' {self._trip_counter} км пробега]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._trip_counter} км пробега'

    @property
    def trip_counter(self):
        return self._trip_counter

    def move(self, distance: int) -> int:
        self.mtbf = self.mtbf
        tbf = ceil(self.mtbf * self._tbf_percent / 100)  # Оставшийся ресурс ТС до поломки
        if distance >= tbf:
            self._trip_counter += tbf
            self.functional = False
            self._tbf_percent = 0
            return tbf
        else:
            self._trip_counter += distance
            self._tbf_percent -= distance / self.mtbf * 100
            return distance
