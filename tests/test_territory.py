import unittest
from src.territory import Territory
from src.player import Player

class TestTerritory(unittest.TestCase):
    def setUp(self):
        self.player = Player(name="John", color="red")


    def test_standard_init(self):
        territory = Territory("Iceland", self.player, 1)
        self.assertEqual(territory.name, "Iceland")
        self.assertEqual(territory.occupied_by, self.player)
        self.assertEqual(territory.num_troops, 1)
    

    def test_unoccupied_no_troops(self):
        territory = Territory("Iceland", None, 0)
        self.assertIsNone(territory.occupied_by)
        self.assertEqual(territory.num_troops, 0)


    def test_occupied_no_troops(self):
        with self.assertRaises(ValueError):
            territory = Territory("Iceland", self.player, 0)


    def test_unoccupied_troops(self):
        with self.assertRaises(ValueError):
            territory = Territory("Iceland", None, 1)


    def test_erroneous_name_type(self):
        with self.assertRaises(TypeError):
            territory = Territory(4, self.player, 1)


    def test_erroneous_occupied_by_type(self):
        with self.assertRaises(TypeError):
            territory = Territory("Iceland", "Player1", 1)


    def test_erroneous_num_troops_type(self):
        with self.assertRaises(TypeError):
            territory = Territory("Iceland", self.player, "1")

    
if __name__ == '__main__':
    unittest.main()