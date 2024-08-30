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

for i in range(10):
    print('\nВсю технику отправляем в поездку на 20.000 км\n')
    fleet.move_all(20000)
    for vehicle in vehicles:
        print(vehicle)
    print('--------------------')
