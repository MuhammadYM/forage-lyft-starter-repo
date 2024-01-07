from serviceable import Serviceable
from engine import Engine
from battery import Battery
from tire_ware import Tire_Ware

class Car(Serviceable):
    def __init__(self, engine:Engine, battery:Battery, tire_ware:Tire_Ware):
        self.engine = engine
        self.battery = battery
        self.tire_ware = tire_ware

    def needs_service(self):
         return self.engine.needs_service() or self.battery.needs_service() or self.tire_ware.tire_needs_service()
