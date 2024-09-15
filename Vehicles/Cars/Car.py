from ..Vehicle import Vehicle
from Resource import Resource

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._type_vehicle = 'наземный'
        self._speed = 90 # [км/ч] средняя скорость
        # Создаем счетчик ресурса с конкретными параметрами, он заменяет None, унаследованное из Vehicle
        self._resource = Resource(40000, 'км')  # 4000 км - ресурс двигателя наземного транспорта

    def __str__(self):
        return super().__str__() + f' {self._trip_counter} км пробега]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._trip_counter} км пробега'

    @property
    def trip_counter(self):
        return self._trip_counter
