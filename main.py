from datetime import date
from car_factory import CarFactory


car1 = CarFactory()
calliope = car1.create_calliope(date(2023, 12, 30), date(2021, 4, 16), 90098, 68201)

print(car1)
print(calliope)