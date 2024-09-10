from ..Vehicle import Vehicle


class Helicopter(Vehicle):
    def __init__(self):
        super().__init__()
        self._type_vehicle = 'воздушный'
        self._fuel = 'бензин'
        self._distance_reserve = 1200
        self._speed = 200 # [км/ч] средняя скорость для пересчёта
        self._name = 'вертолёт'
        self._mtbf = 1000  # [моточасы] двигателя, после которого летательный аппарат ломается
        self._unit = 'ч'

    def __str__(self):
        return super().__str__() + f' {self._hour_counter} часов полёта]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._hour_counter} часов полёта'

    @property
    def hour_counter(self):
        return self._hour_counter
