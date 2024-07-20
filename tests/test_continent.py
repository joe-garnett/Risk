import unittest
from src.continent import Continent
from src.territory import Territory

class TestContinent(unittest.TestCase):
    def setUp(self):
        self.territories = [Territory("Iceland", None, 0), Territory("France", None, 0)]


    def test_standard_init(self):
        continent1 = Continent("Europe", self.territories, 5)
        self.assertEqual(continent1.name, "Europe")
        self.assertEqual(continent1.territories, self.territories)
        self.assertEqual(continent1.troop_bonus, 5)


    def test_erroneous_name_type(self):
        with self.assertRaises(TypeError):
            continent1 = Continent(4, self.territories, 5)


    def test_erroneous_territories_type(self): # i.e not a list
        with self.assertRaises(TypeError):
            continent1 = Continent("Europe", Territory("Iceland", None, 0), 5)
    

    def test_erroneous_type_in_territories(self):
        with self.assertRaises(TypeError):
            continent1 = Continent("Europe", self.territories + ["Iceland"], 5)


    def test_erroneous_troop_bonus_type(self):
        with self.assertRaises(TypeError):
            continent1 = Continent("Europe", self.territories, "5")


    def test_empty_name(self):
        with self.assertRaises(ValueError):
            continent1 = Continent("", self.territories, 5)


    def test_negative_troop_bonus(self):
        with self.assertRaises(ValueError):
            continent1 = Continent("Europe", self.territories, -2)