from datetime import date
from engine import CapuletEngine
from battery import SpinderBattery
from car import Car
class CarFactory:
    def create_calliope(self,current_date,last_service_date,current_mileage,last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date

        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SpinderBattery(last_service_mileage,current_mileage)

        return Car(engine,battery) 
    