from abc import ABC


class Tire_Ware(ABC):
    def __init__(self,tire_ware_sensor) -> None:
        self.tire_ware_sensor = tire_ware_sensor

    def tire_needs_service(self):
        pass

class Carigan_Tire(Tire_Ware):
    def __init__(self, tire_ware_sensor) -> None:
        super().__init__(tire_ware_sensor)
    
    def tire_needs_service(self):
        ware_count = 0
        for value in self.tire_ware_sensor:
            if value >= 0.9:
                ware_count+=1

        return ware_count>=1
    
class Octoprime_Tire(Tire_Ware):
    def __init__(self, tire_ware_sensor) -> None:
        super().__init__(tire_ware_sensor)
    
    def tire_needs_service(self):
        sum = 0
        for value in self.tire_ware_sensor:
            sum+=value
                
        return sum>=3
            