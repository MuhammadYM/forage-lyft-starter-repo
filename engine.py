class Engine:
    def __init__(self) -> None:
        pass
        
    def needs_service():
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage:int,current_mileage:int) -> None:
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage:int,current_mileage:int) -> None:
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on:bool) -> None:
        self.warning_light_is_on = warning_light_is_on
    
    def needs_service(self):
        return self.warning_light_is_on