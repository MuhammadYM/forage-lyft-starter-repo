from datetime import date
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpinderBattery, NubbinBattery
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
    
    def create_glissade(self,current_date,last_service_date,current_mileage,last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date

        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SpinderBattery(last_service_mileage,current_mileage)

        return Car(engine,battery)
    

    def create_palindrome(self,current_date,last_service_date, warning_light_on):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on

        engine = SternmanEngine(warning_light_on)
        battery = SpinderBattery(last_service_date,current_date)

        return Car(engine,battery)

    
    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date

        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)

        return Car(engine,battery)
    
    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date

        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)

        return Car(engine,battery)