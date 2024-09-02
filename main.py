from Vehicles.Cars.PetrolCar import PetrolCar
from Vehicles.Cars.ElectroCar import ElectroCar
from Vehicles.AirVehicles.Helicopter import Helicopter
from Vehicles.Watercrafts.SpeedBoat import SpeedBoat
from Vehicles.Watercrafts.CruiseShip import CruiseShip
from Fleet import Fleet

pc = PetrolCar()
ec = ElectroCar()
heli = Helicopter()
sb = SpeedBoat()
cs = CruiseShip()

vehicles = (pc, ec, heli, sb, cs)

fleet = Fleet()
for vehicle in vehicles:
    fleet.add_vehicle(vehicle)

dist = 100000
print(f'\nВсю технику отправляем в поездку на {dist} км\n')
# Добьемся того, чтобы весь парк техники проехал весь путь.
# Пусть Fleet обеспечивает движение и починку - это его ответственность.
fleet.move_all(dist)
for vehicle in vehicles:
    print(vehicle)
print('--------------------')
