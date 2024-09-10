from ..Vehicle import Vehicle


class Watercraft(Vehicle):
    def __init__(self):
        super().__init__()
        self._type_vehicle = 'водный'
        self._mtbf = 1000  # [моточасы] двигателя, после которого лодка ломается
        self._unit = 'ч'

    def __str__(self):
        return super().__str__() + f' {self._hour_counter} часов следования]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._hour_counter} часов следования'

    @property
    def hour_counter(self):
        return self._hour_counter
