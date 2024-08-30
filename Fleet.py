from random import choice
from Vehicles.Vehicle import Vehicle


class Fleet:
    def __init__(self):
        self._vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self._vehicles.append(vehicle)

    def move_all(self, distance):
        for vehicle in self._vehicles:
            vehicle.move(distance)
