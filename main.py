from datetime import date
from car_factory import CarFactory
from engine import CapuletEngine

car1 = CarFactory()
calliope = car1.create_calliope(date(2023, 12, 30), date(2021, 4, 16), 90098, 68201)
calliope.engine = CapuletEngine(1200,1300)
print(car1)
print(calliope.engine.needs_service())