from .Vehicle import Vehicle
from math import ceil


class MotoHoursVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        self._hour_counter = 0  # [моточасы] счётчик пробега

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
