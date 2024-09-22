from math import ceil


class MotoHoursVehicle:
    def __init__(self):
        super().__init__()
        self._hour_counter = 0  # [моточасы] счётчик пробега
        self._speed = 0 # средняя скорость
        self._resource = None  # Потомки определят ресурс двигателя (водного или воздушного транспорта)

    @property
    def resource(self):
        return self._resource

    def move(self, distance: float) -> float:
        """Движение на заданное расстояние.
        Args:
            distance: запрошенное расстояние, которое нужно пройти.
        Returns:
            Реально пройденное расстояние. Оно может быть меньше, чем запрошенное, если машина сломалась в пути
        """
        actually_hour = self.resource.spend(distance / self._speed)
        self._hour_counter += ceil(actually_hour)
        return actually_hour * self._speed
