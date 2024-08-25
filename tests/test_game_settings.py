import unittest
from src.game_settings import GameSettings  

class TestGameSettings(unittest.TestCase):

    def test_standard_init(self):
        game_settings1 = GameSettings(2, "auto", "balanced_blitz", "static", True, False, False, "standard")
        self.assertEqual(game_settings1.num_players, 2)
        self.assertEqual(game_settings1.placement, "auto")
        self.assertEqual(game_settings1.dice_rolls, "balanced_blitz")
        self.assertEqual(game_settings1.card_bonus_multiplier, "static")
        self.assertEqual(game_settings1.is_blizzards, True)
        self.assertEqual(game_settings1.is_fog_of_war, False)
        self.assertEqual(game_settings1.is_portals, False)
        self.assertEqual(game_settings1.map, "standard")

    
    def test_erroneous_num_players_type(self):
        with self.assertRaises(TypeError):
            game_settings1 = GameSettings("2", "auto", "balanced_blitz", "static", True, False, False, "standard")

    
    def test_erroneous_placement_type(self):
        with self.assertRaises(TypeError):
            game_settings1 = GameSettings(2, 4, "balanced_blitz", "static", True, False, False, "standard")


    def test_erroneous_dice_rolls_type(self):
        with self.assertRaises(TypeError):
            game_settings1 = GameSettings(2, "auto", 4, "static", True, False, False, "standard")


    def test_erroneous_card_bonus_multiplier_type(self):
        with self.assertRaises(TypeError):
            game_settings1 = GameSettings(2, "auto", "balanced_blitz", 5, True, False, False, "standard")

    
    def test_erroneous_is_blizzards_type(self):
        with self.assertRaises(TypeError):
            game_settings1 = GameSettings(2, "auto", "balanced_blitz", "static", "True", False, False, "standard")


    def test_erroneous_is_fog_of_war_type(self):
        with self.assertRaises(TypeError):
            game_settings1 = GameSettings(2, "auto", "balanced_blitz", "static", True, "False", False, "standard")


    def test_erroneous_is_portals_type(self):
        with self.assertRaises(TypeError):
            game_settings1 = GameSettings(2, "auto", "balanced_blitz", "static", True, False, "False", "standard")


    def test_erroneous_map_type(self):
        with self.assertRaises(TypeError):
            game_settings1 = GameSettings(2, "auto", "balanced_blitz", "static", True, False, False, 4)


    def test_erroneous_num_players_value(self):
        with self.assertRaises(ValueError):
            game_settings1 = GameSettings(0, "auto", "balanced_blitz", "static", True, False, False, "standard")


    def test_erroneous_placement_value(self):
        with self.assertRaises(ValueError):
            game_settings1 = GameSettings(2, "random", "balanced_blitz", "static", True, False, False, "standard")


    def test_erroneous_dice_rolls_value(self):
        with self.assertRaises(ValueError):
            game_settings1 = GameSettings(2, "auto", "random", "static", True, False, False, "standard")

    
    def test_erroneous_card_bonus_multiplier_value(self):
        with self.assertRaises(ValueError):
            game_settings1 = GameSettings(2, "auto", "balanced_blitz", "dynamic", True, False, False, "standard")

    
    def test_erroneous_map_value(self):
        with self.assertRaises(ValueError):
            game_settings1 = GameSettings(2, "auto", "balanced_blitz", "static", True, False, False, "USA")

    
    
    
   