import unittest
from datetime import date
from car_factory import CarFactory
from engine import CapuletEngine, WilloughbyEngine,SternmanEngine
from battery import SpinderBattery, NubbinBattery

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car1 = CarFactory()
        calliope = car1.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        calliope.battery = SpinderBattery(last_service_date,today)
        self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car1 = CarFactory()
        calliope = car1.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        calliope.battery = SpinderBattery(last_service_date,today)
        self.assertFalse(calliope.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 300001
        last_service_mileage = 0

        car2 = CarFactory()
        calliope = car2.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        calliope.engine = CapuletEngine(last_service_mileage, current_mileage)

        self.assertTrue(calliope.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 30000
        last_service_mileage = 0

        car3 = CarFactory()
        calliope = car3.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        calliope.battery = SpinderBattery(last_service_date,today)
        calliope.engine = CapuletEngine(last_service_mileage, current_mileage)
    
        self.assertFalse(calliope.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car1 = CarFactory()
        glissade = car1.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        glissade.battery = SpinderBattery(last_service_date,today)
        self.assertTrue(glissade.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car1 = CarFactory()
        glissade = car1.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        glissade.battery = SpinderBattery(last_service_date,today)
        self.assertFalse(glissade.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 600001
        last_service_mileage = 0

        car2 = CarFactory()
        glissade = car2.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        glissade.engine = WilloughbyEngine(last_service_mileage, current_mileage)

        self.assertTrue(glissade.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 60000
        last_service_mileage = 0

        car3 = CarFactory()
        glissade = car3.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        glissade.battery = SpinderBattery(last_service_date,today)
        glissade.engine = WilloughbyEngine(last_service_mileage, current_mileage)

        self.assertFalse(glissade.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_on = False

        car1 = CarFactory()
        palindrome = car1.create_palindrome(today, last_service_date, warning_light_on)
        palindrome.battery = SpinderBattery(last_service_date,today)
        self.assertTrue(palindrome.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False

        car1 = CarFactory()
        palindrome = car1.create_palindrome(today, last_service_date, warning_light_on)
        palindrome.battery = SpinderBattery(last_service_date, today)
        self.assertFalse(palindrome.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        warning_light_is_on = True

        car1 = CarFactory()
        palindrome = car1.create_palindrome(today, last_service_date, warning_light_is_on)
        palindrome.engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(palindrome.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        warning_light_is_on = False

        car1 = CarFactory()
        palindrome = car1.create_palindrome(today, last_service_date, warning_light_is_on)
        palindrome.engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(palindrome.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car1 = CarFactory()
        rorschach = car1.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        rorschach.battery = NubbinBattery(last_service_date,today)
        self.assertTrue(rorschach.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car1 = CarFactory()
        rorschach = car1.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        rorschach.battery = NubbinBattery(last_service_date,today)
        self.assertFalse(rorschach.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 600001
        last_service_mileage = 0

        car2 = CarFactory()
        rorschach = car2.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        rorschach.engine = WilloughbyEngine(last_service_mileage, current_mileage)

        self.assertTrue(rorschach.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 60000
        last_service_mileage = 0

        car3 = CarFactory()
        rorschach = car3.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        rorschach.battery = NubbinBattery(last_service_date,today)
        rorschach.engine = WilloughbyEngine(last_service_mileage, current_mileage)

        self.assertFalse(rorschach.needs_service())

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car1 = CarFactory()
        thovex = car1.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        thovex.battery = NubbinBattery(last_service_date,today)
        self.assertTrue(thovex.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car1 = CarFactory()
        rorschach = car1.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        rorschach.battery = NubbinBattery(last_service_date,today)
        self.assertFalse(rorschach.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 300001
        last_service_mileage = 0

        car2 = CarFactory()
        thovex = car2.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        thovex.engine = CapuletEngine(last_service_mileage, current_mileage)

        self.assertTrue(thovex.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = date.today()
        current_mileage = 30000
        last_service_mileage = 0

        car3 = CarFactory()
        thovex = car3.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        thovex.battery = NubbinBattery(last_service_date,today)
        thovex.engine = CapuletEngine(last_service_mileage, current_mileage)
    
        self.assertFalse(thovex.needs_service())

    

if __name__ == '__main__':
        unittest.main()