import unittest
from src.continent import Continent
from src.territory import Territory
from src.player import Player

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

    
    def test_empty_territories_list(self):
        with self.assertRaises(ValueError):
            continent1 = Continent("Europe", [], 5)

    
    def test_occupied_by_method(self):
        player1 = Player("John", "red")
        territories1 = [Territory("Iceland", player1, 2), Territory("France", player1, 2)]
        continent1 = Continent("Europe", territories1, 5)
        
        player2 = Player("Frank", "blue")
        territories2 = [Territory("Iceland", player1, 2), Territory("France", player2, 2)]
        continent2 = Continent("Europe", territories2, 5)
        
        self.assertEqual(continent1.occupied_by(), player1)
        self.assertEqual(continent2.occupied_by(), None)