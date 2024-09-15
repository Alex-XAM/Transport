from math import ceil
from typing import Callable

class Resource:
    """Класс хранит остаток межремонтного ресурса транспортного средства"""
    def __init__(self, mtbf: int, unit: str):
        # Средний остаток ресурса до следующего ремонта. Не менять за время жизни объекта.
        # Единицы измерения (км, часы, ...) не имеют значения, пусть использующий класс сам знает о единицах.
        self._mtbf = mtbf
        # Единица измерения ресурса. Только для красивого вывода в __str__
        self._unit = unit
        # Оставшийся процент TBF, то есть сколько процентов от номинального значения MTBF осталось до поломки.
        # Когда это значение упадет до нуля, машина ломается.
        self._tbf_percent = 100.0
        # Количество ремонтов. Используется для того, чтобы межремонтный пробег уменьшался с каждым ремонтом.
        self._repairs = 0

    def __str__(self):
        return f'Остаток ресурса {ceil(self.units_left)} {self._unit}'

    @property
    def units_left(self) -> float:
        """Возвращает остаток ресурса"""
        return self._mtbf * self._tbf_percent / 100.0

    @property
    def functional(self) -> bool:
        return bool(self._tbf_percent)

    def spend(self, x: float) -> float:
        """Тратит x единиц ресурса. Возвращает реально потраченное количество."""
        x_percents = x / self._mtbf * 100.0  # x, выраженное в процентах
        if x_percents < self._tbf_percent:
            actually_spent = x
            self._tbf_percent -= x_percents
        else:
            actually_spent = self._tbf_percent * self._mtbf / 100.0
            self._tbf_percent = 0.0
        assert self._tbf_percent >= 0.0, 'Процент TBF не может быть отрицательным'
        assert actually_spent <= x, 'Потрачено больше, чем требовалось'
        return actually_spent

    def fix(self):
        """Ремонтирует ТС, восстанавливает ресурс до номинального значения"""
        self._repairs += 1
        self._tbf_percent = 100.0 - self._repairs * 5.0  # При каждом ремонте запас ресурса падает на 5%
        if self._tbf_percent <= 0:
            self._tbf_percent = 0.0
            raise ValueError('Транспортное средство выработало свой ресурс')
