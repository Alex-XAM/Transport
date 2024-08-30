class Vehicle:
    def __init__(self):
        self._fuel = 'не определено'
        self._distance_reserve = 0
        self._speed = 0 # средняя скорость
        self._name = 'не определено'
        self._functional = True

    def __str__(self):
        f = ('' if self._functional else 'не') + 'исправен'
        return f'{self._name} [{self._fuel}, {f}]'

    @property
    def fuel(self):
        return self._fuel

    @property
    def functional(self):
        return self._functional

    @functional.setter
    def functional(self, functional: bool):
        self._functional = bool(functional)
