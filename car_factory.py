from datetime import date
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpinderBattery, NubbinBattery
from car import Car
from tire_ware import Carigan_Tire, Octoprime_Tire
class CarFactory:
    def create_calliope(self,current_date,last_service_date,current_mileage,last_service_mileage,tire_ware_sensor):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
        self.tire_ware_sensor = tire_ware_sensor

        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SpinderBattery(last_service_mileage,current_mileage)
        tire_ware = Carigan_Tire(tire_ware_sensor)

        return Car(engine,battery,tire_ware) 
    
    def create_glissade(self,current_date,last_service_date,current_mileage,last_service_mileage,tire_ware_sensor):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
        self.tire_ware_sensor = tire_ware_sensor

        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SpinderBattery(last_service_mileage,current_mileage)
        tire_ware = Carigan_Tire(tire_ware_sensor)

        return Car(engine,battery,tire_ware) 
    

    def create_palindrome(self,current_date,last_service_date, warning_light_on,tire_ware_sensor):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on
        self.tire_ware_sensor = tire_ware_sensor

        engine = SternmanEngine(warning_light_on)
        battery = SpinderBattery(last_service_date,current_date)
        tire_ware = Carigan_Tire(tire_ware_sensor)

        return Car(engine,battery,tire_ware) 

    
    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage, tire_ware_sensor):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
        self.tire_ware_sensor = tire_ware_sensor

        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tire_ware = Octoprime_Tire(tire_ware_sensor)

        return Car(engine,battery,tire_ware)
    
    def create_thovex(self,current_date,last_service_date,current_mileage,last_service_mileage, tire_ware_sensor):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
        self.tire_ware_sensor = tire_ware_sensor

        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tire_ware = Octoprime_Tire(tire_ware_sensor)

        return Car(engine,battery,tire_ware)