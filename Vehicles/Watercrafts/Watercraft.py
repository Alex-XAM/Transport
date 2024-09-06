from ..Vehicle import Vehicle


class Watercraft(Vehicle):
    def __init__(self):
        super().__init__()
        self._type_vehicle = 'водный'
        self._mtbf = 1000  # [моточасы] двигателя, после которого лодка ломается
        # mtbf_after_repair - значение MTBF после ремонта ТС
        # Первое значение будет искомое значение MTBF, а далее значение уменьшится
        self._mtbf_after_repair = self.mtbf

    def __str__(self):
        return super().__str__() + f' {self._hour_counter} часов следования]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._hour_counter} часов следования'

    @property
    def hour_counter(self):
        return self._hour_counter
