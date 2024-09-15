from math import ceil


class Vehicle:
    def __init__(self):
        self._fuel = 'не определено'
        self._distance_reserve = 0
        self._speed = 0 # средняя скорость
        self._name = 'не определено'
        self._type_vehicle = 'не определено'
        self._trip_counter = 0  # [км] счётчик пробега
        self._hour_counter = 0  # [моточасы] счётчик пробега
        # Все, что было связано с обработкой ресурса и поломок, из этого класса убираем. Взамен будет экземпляр
        # класса Resource. Будем им пользоваться для всей работы с поломками. Но здесь (в классе Vehicle) экземпляр
        # Resource не создаём потому, что только классы-потомки знают, с какими параметрами надо создавать
        # экземпляр Resource. Вместо экземпляра Resource написано None. Не очень красиво, но пока так,
        # потом сделаем лучше.
        self._resource = None  # Классы-потомки пропишут в это поле экземпляр Resource

    def __str__(self):
        f = ('' if self._resource.functional else 'не') + 'исправен'
        return f'{self._name} [{self._fuel}, {f}'

    @property
    def name(self):
        return self._name

    @property
    def resource(self):
        return self._resource

    @property
    def type_vehicle(self):
        return self._type_vehicle

    @property
    def fuel(self):
        return self._fuel

    @property
    def functional(self):
        # Обертка вокруг functional из счетчика ресурса
        return self._resource.functional

    def fix(self):
        # Обертка вокруг fix() из счетчика ресурса
        self._resource.fix()

    def move(self, distance: float) -> float:
        """Движение на заданное расстояние.
        Args:
            distance: запрошенное расстояние, которое нужно пройти.
        Returns:
            Реально пройденное расстояние. Оно может быть меньше, чем запрошенное, если машина сломалась в пути
        """

        if self.type_vehicle == 'наземный':
            actually_distance = self._resource.spend(distance)
            self._trip_counter += ceil(actually_distance)
            return actually_distance
        else:
            actually_hour = self._resource.spend(distance / self._speed)
            self._hour_counter += ceil(actually_hour)
            return actually_hour * self._speed
