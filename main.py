from engine.model.calliope import Calliope
from engine.model.palindrome import Palindrome

car1 = Calliope(12,4300,13)
car2 = Palindrome(2022, True)
print(car1.engine_should_be_serviced())
print(car2.engine_should_be_serviced())