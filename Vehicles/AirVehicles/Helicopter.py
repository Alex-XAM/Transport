from ..Vehicle import Vehicle
from Resource import Resource
from ..MotoHoursVehicle import MotoHoursVehicle


class Helicopter(MotoHoursVehicle, Vehicle):
    def __init__(self):
        super().__init__()
        self._fuel = 'бензин'
        self._distance_reserve = 1200
        self._speed = 200 # [км/ч] средняя скорость для пересчёта
        self._name = 'вертолёт'
        self._resource = Resource(1000, 'ч')  # 1000 ч - ресурс двигателя вертолёта

    def __str__(self):
        return super().__str__() + f' {self._hour_counter} часов полёта]'

    @property
    def resource(self):
        return self._resource

    @property
    def operating_hours(self):
        return f'{self._name}: {self._hour_counter} часов полёта'

    @property
    def hour_counter(self):
        return self._hour_counter
