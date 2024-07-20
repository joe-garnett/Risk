import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def test_standard_init(self):
        card1 = Card("artillery")
        self.assertEqual(card1.type, "artillery")


    def test_erroneous_card_type(self):
        with self.assertRaises(ValueError):
            card1 = Card("gunner")