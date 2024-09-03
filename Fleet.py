from Vehicles.Vehicle import Vehicle


class Fleet:
    def __init__(self):
        self._vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self._vehicles.append(vehicle)

    def move_all(self, distance):
        for vehicle in self._vehicles:
            print(f'{vehicle.name} начал движение на дистанцию {distance} км')
            rest_of_distance = distance
            while rest_of_distance:
                rest_of_distance -= vehicle.move(rest_of_distance)
                print(f'{vehicle.name} достиг отметки {distance - rest_of_distance} км')
                if not vehicle.functional:
                    print(f'{vehicle.name} неисправен')
                    self.repair_vehicle(vehicle)
            print()

    def repair_vehicle(self, vehicle: Vehicle):
        vehicle.functional = True
        vehicle._tbf_percent = 100
        print(f'{vehicle.name} отремонтирован')
