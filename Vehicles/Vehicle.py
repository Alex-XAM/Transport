from math import ceil

from Transport.Resource import Resource


class Vehicle(Resource):
    def __init__(self):
        self._name = 'не определено'
        self._fuel = 'не определено'
        self._type_vehicle = 'не определено'
        self._unit = 'не определено'
        self._distance_reserve = 0
        self._speed = 0 # средняя скорость
        self._trip_counter = 0  # [км] счётчик пробега
        self._hour_counter = 0  # [моточасы] счётчик пробега
        self._mtbf = 0  # MTBF (Mean time between failures) - средняя наработка на отказ.
        self._tbf_percent = 100  # Оставшийся процент TBF, то есть сколько процентов от номинального значения MTBF осталось до поломки.
        super().__init__(self.mtbf, self._unit)

    def __str__(self):
        f = ('' if self._functional else 'не') + 'исправен'
        return f'{self._name} [топливо: {self._fuel}, {f},'

    @property
    def name(self):
        return self._name

    @property
    def unit(self):
        return self._unit

    @property
    def trip_counter(self):
        return self._trip_counter

    @property
    def hour_counter(self):
        return self._hour_counter

    @property
    def type_vehicle(self):
        return self._type_vehicle

    @property
    def tbf_percent(self):
        return self._tbf_percent

    @property
    def fuel(self):
        return self._fuel

    @property
    def mtbf(self):
        return self._mtbf

    def move(self, distance: float) -> float:
        """Движение на заданное расстояние.
        Args:
            distance: запрошенное расстояние, которое нужно пройти.
        Returns:
            Реально пройденное расстояние. Оно может быть меньше, чем запрошенное, если машина сломалась в пути
        """
        if self.type_vehicle == 'наземный':
            actually_dist = self.spend(distance)
            self._trip_counter += actually_dist
            return actually_dist
        else:
            hour = ceil(distance / self._speed)  # Количество часов необходимых для прохождения дистанции
            actually_hour = float(self.spend(hour))
            self._hour_counter += actually_hour
            return actually_hour * self._speed if hour > actually_hour else distance
