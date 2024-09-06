from math import ceil
from random import randint


class Vehicle:
    def __init__(self):
        self._fuel = 'не определено'
        self._distance_reserve = 0
        self._speed = 0 # средняя скорость
        self._name = 'не определено'
        self._type_vehicle = 'не определено'
        self._trip_counter = 0  # [км] счётчик пробега
        self._hour_counter = 0  # [моточасы] счётчик пробега
        # Выносим функционал описания поломок в базовый класс. Используем два параметра.
        # 1. MTBF (Mean time between failures) - средняя наработка на отказ.
        # В данном случае это сколько в среднем механизм отработает до поломки. Единицы измерения -
        # те, которые применимы для конкретного класса (км, часы и т.п.). Значения установить в
        # конструкторах конкретных классов.
        self._mtbf = 0
        # 2. Оставшийся процент TBF, то есть сколько процентов от номинального значения MTBF осталось до поломки.
        # Когда это значение упадет до нуля, машина ломается. Это работает одинаково для всех классов.
        # Пробег до поломки будет равен произведению этих двух величин. Например,
        #  self._mtbf == 40000 и self._tbf_percent == 10, тогда машина сломается через 4000 пробега.
        self._tbf_percent = 100
        self._functional = True
        # И вызовем "починку" машины, чтобы правильно инициализировать параметры, связанные с поломками
        # self.functional = True
        # mtbf_after_repair - значение MTBF после ремонта ТС
        # Первое значение будет искомое значение MTBF, а далее значение уменьшится
        self._mtbf_after_repair = 0

    def __str__(self):
        f = ('' if self._functional else 'не') + 'исправен'
        return f'{self._name} [{self._fuel}, {f}'

    @property
    def name(self):
        return self._name

    @property
    def type_vehicle(self):
        return self._type_vehicle

    @property
    def mtbf_after_repair(self):
        return self._mtbf_after_repair

    @property
    def tbf_percent(self):
        return self._tbf_percent

    @property
    def fuel(self):
        return self._fuel

    @property
    def functional(self):
        return self._functional

    @property
    def mtbf(self):
        return self._mtbf

    @mtbf_after_repair.setter
    def mtbf_after_repair(self, mtbf):
        """Значение mtbf_after_repair после ремонта будет от 77 до 99% значения MTBF"""
        percents = (77, 99)
        percent1, percent2 = [ceil(mtbf / 100 * p) for p in percents]
        self._mtbf_after_repair = randint(percent1, percent2)

    @functional.setter
    def functional(self, functional: bool):
        """Установка состояния исправной или поломанной машины и связанных с этим значений"""
        self._functional = bool(functional)
        # Если машину починили, то TBF поднимаем до полного значения
        if self._functional:
            self._tbf_percent = 100
            self.mtbf_after_repair = self.mtbf

    def move(self, distance: int, type_vehicle: str) -> int:
        """Движение на заданное расстояние.
        Args:
            distance: запрошенное расстояние, которое нужно пройти.
        Returns:
            Реально пройденное расстояние. Оно может быть меньше, чем запрошенное, если машина сломалась в пути
        """
        tbf = ceil(self.mtbf_after_repair * self.tbf_percent / 100)  # [км] или [моточасы] Оставшийся ресурс ТС до поломки
        if type_vehicle == 'наземный':
            if distance >= tbf:
                self._trip_counter += tbf
                self.functional = False
                self._tbf_percent = 0
                return tbf
            else:
                self._trip_counter += distance
                self._tbf_percent -= distance / self.mtbf_after_repair * 100
                return distance
        else:
            hour = ceil(distance / self._speed)  # Количество часов необходимых для прохождения дистанции
            if hour >= tbf:
                self._hour_counter += tbf
                self.functional = False
                self._tbf_percent = 0
                return tbf * self._speed
            else:
                self._hour_counter += hour
                self._tbf_percent -= hour / self.mtbf_after_repair * 100
                return distance
