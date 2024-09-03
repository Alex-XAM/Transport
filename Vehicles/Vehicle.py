from math import ceil
from random import randint


class Vehicle:
    def __init__(self):
        self._fuel = 'не определено'
        self._distance_reserve = 0
        self._speed = 0 # средняя скорость
        self._name = 'не определено'
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
        self.functional = True

    def __str__(self):
        f = ('' if self._functional else 'не') + 'исправен'
        return f'{self._name} [{self._fuel}, {f}'

    @property
    def name(self):
        return self._name

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

    @mtbf.setter
    def mtbf(self, mtbf):
        p = 10  # Разбег в пробеге 10%
        percent = ceil(self.mtbf / 100 * p)
        self._mtbf = randint(self.mtbf - percent, self.mtbf + percent)  # self.mtbf +- 10%

    @functional.setter
    def functional(self, functional: bool):
        """Установка состояния исправной или поломанной машины и связанных с этим значений"""
        self._functional = bool(functional)
        # Если машину починили, то TBF поднимаем до полного значения
        if self._functional:
            self._tbf_percent = 100

    def move(self, distance: int) -> int:
        """Движение на заданное расстояние.
        Args:
            distance: запрошенное расстояние, которое нужно пройти.
        Returns:
            Реально пройденное расстояние. Оно может быть меньше, чем запрошенное, если машина сломалась в пути
        """
        return 0
