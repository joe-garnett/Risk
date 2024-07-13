import unittest
from src.player import Player

class TestTerritory(unittest.TestCase):
    def test_standard_init(self):
        player1 = Player("John", "red")
        self.assertEqual(player1.name, "John")
        self.assertEqual(player1.color, "red")


    def test_impossible_color(self):
        with self.assertRaises(ValueError):
            player2 = Player("John", "lilac")


    def test_erroneous_name_type(self):
        with self.assertRaises(TypeError):
            player1 = Player(4, "red")


    def test_erroneous_color_type(self):
        with self.assertRaises(TypeError):
            player1 = Player("John", None)