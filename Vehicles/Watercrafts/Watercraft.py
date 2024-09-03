from math import ceil
from ..Vehicle import Vehicle


class Watercraft(Vehicle):
    def __init__(self):
        super().__init__()
        self._hour_counter = 0  # [моточасы] счётчик пробега
        self._mtbf = 1000  # [моточасы] двигателя, после которого лодка ломается

    def __str__(self):
        return super().__str__() + f' {self._hour_counter} часов следования]'

    @property
    def operating_hours(self):
        return f'{self._name}: {self._hour_counter} часов следования'

    @property
    def hour_counter(self):
        return self._hour_counter

    def move(self, distance: int) -> int:
        self.mtbf = self.mtbf
        tbf = ceil(self.mtbf * self._tbf_percent / 100)  # [моточасы] Оставшийся ресурс ТС до поломки
        hour = ceil(distance / self._speed)  # Количество часов необходимых для прохождения дистанции
        if hour >= tbf:
            self._hour_counter += tbf
            self.functional = False
            self._tbf_percent = 0
            return tbf * self._speed
        else:
            self._hour_counter += hour
            self._tbf_percent -= hour / self.mtbf * 100
            return distance
