from ..Vehicle import Vehicle
from Resource import Resource
from math import ceil

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._speed = 90 # [км/ч] средняя скорость
        self._trip_counter = 0  # [км] счётчик пробега
        self._resource = Resource(40000, 'км')  # 4000 км - ресурс двигателя наземного транспорта

    def __str__(self):
        return super().__str__() + f' {self._trip_counter} км пробега]'

    @property
    def resource(self):
        return self._resource

    @property
    def operating_hours(self):
        return f'{self._name}: {self._trip_counter} км пробега'

    @property
    def trip_counter(self):
        return self._trip_counter

    def move(self, distance: float) -> float:
        """Движение на заданное расстояние.
        Args:
            distance: запрошенное расстояние, которое нужно пройти.
        Returns:
            Реально пройденное расстояние. Оно может быть меньше, чем запрошенное, если машина сломалась в пути
        """
        actually_distance = self.resource.spend(distance)
        self._trip_counter += ceil(actually_distance)
        return actually_distance
