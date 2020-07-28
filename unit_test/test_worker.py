from unittest import TestCase
from datetime import *
from unit_test.worker import *

class TestWorker(TestCase):

    def test_age(self):
        bob= Worker('bob','cohen',1980,1,1,'1 yigal alon, Tel Aviv','il')
        self.assertIn('40',bob.age())

    def test_age2(self):
        mati=Worker('mati','levi',2021,1,1,1, 'yigal alon, Tel Aviv','il')
        self.assertIn('-1', mati.age())

    def test_age3(self):
        mati = Worker('mati', 'levi', 2020, 1, 1, 1, 'yigal alon, Tel Aviv', 'il')
        self.assertIn('0', mati.age())

    def test_days_to_birthday(self):
        self.fail()

    def test_greet(self):
        self.fail()

    def test_location(self):
        self.fail()

