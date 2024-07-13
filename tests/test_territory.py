import unittest
from src.territory import Territory

class TestTerritory(unittest.TestCase):
    def test_standard_init(self):
        territory = Territory("Iceland", "Player1", 1)
        self.assertEqual(territory.name, "Iceland")
        self.assertEqual(territory.occupied_by, "Player1")
        self.assertEqual(territory.num_troops, 1)
    

    def test_unoccupied_no_troops(self):
        territory = Territory("Iceland", None, 0)
        self.assertIsNone(territory.occupied_by)
        self.assertEqual(territory.num_troops, 0)


    def test_occupied_no_troops(self):
        with self.assertRaises(ValueError):
            territory = Territory("Iceland", "Player1", 0)


    def test_unoccupied_troops(self):
        with self.assertRaises(ValueError):
            territory = Territory("Iceland", None, 1)


if __name__ == '__main__':
    unittest.main()