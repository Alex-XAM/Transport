from ..Vehicle import Vehicle
from Resource import Resource


class Watercraft(Vehicle):
    def __init__(self):
        super().__init__()
        self._type_vehicle = 'водный'
        # Создаем счетчик ресурса с конкретными параметрами, он заменяет None, унаследованное из Vehicle
        self._resource = Resource(1000, 'ч')  # 1000 ч - ресурс двигателя водного транспорта

    def __str__(self):
        return super().__str__() + f' {self._hour_counter} часов следования]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._hour_counter} часов следования'

    @property
    def hour_counter(self):
        return self._hour_counter
