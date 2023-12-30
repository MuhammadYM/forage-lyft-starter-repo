from datetime import date


class Battery:
    def __init__(self) -> None:
        pass

    def needs_service(self):
        pass


class SpinderBattery(Battery):
    def __init__(self,last_service_date:date, current_date:date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return self.current_date > service_threshold_date
    
class NubbinBattery(Battery):
    def __init__(self,last_service_date:date, current_date:date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return self.current_date > service_threshold_date
        