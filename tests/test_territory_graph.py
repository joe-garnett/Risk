import unittest
from src.territory_graph import TerritoryGraph
from src.game_settings import GameSettings
from src.territory import Territory

# test erroneous game settings type
# test get_neighbors valid
# test get
class TestTerritoryGraph(unittest.TestCase):
    def setUp(self):
        self.standard_territory_graph = {
        "Alaska": ["Northwest Territory", "Alberta", "Kamchatka"],
        "Northwest Territory": ["Alaska", "Alberta", "Ontario", "Greenland"],
        "Alberta": ["Alaska", "Northwest Territory", "Ontario", "Western United States"],
        "Ontario": ["Northwest Territory", "Alberta", "Western United States", "Eastern United States", "Quebec", "Greenland"],
        "Western United States": ["Alberta", "Ontario", "Eastern United States", "Central America"],
        "Eastern United States": ["Ontario", "Western United States", "Quebec", "Central America"],
        "Quebec": ["Ontario", "Eastern United States", "Greenland"],
        "Greenland": ["Northwest Territory", "Ontario", "Quebec", "Iceland"],
        "Central America": ["Western United States", "Eastern United States", "Venezuela"],
        "Venezuela": ["Central America", "Peru", "Brazil"],
        "Peru": ["Venezuela", "Brazil", "Argentina"],
        "Brazil": ["Venezuela", "Peru", "Argentina", "North Africa"],
        "Argentina": ["Peru", "Brazil"],
        "North Africa": ["Brazil", "Egypt", "East Africa", "Congo", "Western Europe", "Southern Europe"],
        "Egypt": ["North Africa", "East Africa", "Southern Europe", "Middle East"],
        "East Africa": ["North Africa", "Egypt", "Congo", "South Africa", "Madagascar", "Middle East"],
        "Congo": ["North Africa", "East Africa", "South Africa"],
        "South Africa": ["Congo", "East Africa", "Madagascar"],
        "Madagascar": ["East Africa", "South Africa"],
        "Western Europe": ["North Africa", "Southern Europe", "Great Britain", "Northern Europe"],
        "Southern Europe": ["Western Europe", "North Africa", "Egypt", "Middle East", "Ukraine", "Northern Europe"],
        "Northern Europe": ["Western Europe", "Southern Europe", "Great Britain", "Scandinavia", "Ukraine"],
        "Great Britain": ["Iceland", "Scandinavia", "Northern Europe", "Western Europe"],
        "Iceland": ["Greenland", "Great Britain", "Scandinavia"],
        "Scandinavia": ["Iceland", "Great Britain", "Northern Europe", "Ukraine"],
        "Ukraine": ["Scandinavia", "Northern Europe", "Southern Europe", "Middle East", "Afghanistan", "Ural"],
        "Middle East": ["Ukraine", "Southern Europe", "Egypt", "East Africa", "Afghanistan", "India"],
        "Afghanistan": ["Ukraine", "Ural", "China", "India", "Middle East"],
        "Ural": ["Ukraine", "Afghanistan", "China", "Siberia"],
        "Siberia": ["Ural", "China", "Mongolia", "Irkutsk", "Yakutsk"],
        "Yakutsk": ["Siberia", "Irkutsk", "Kamchatka"],
        "Kamchatka": ["Yakutsk", "Irkutsk", "Mongolia", "Japan", "Alaska"],
        "Irkutsk": ["Siberia", "Yakutsk", "Kamchatka", "Mongolia"],
        "Mongolia": ["Siberia", "Irkutsk", "Kamchatka", "Japan", "China"],
        "Japan": ["Mongolia", "Kamchatka"],
        "China": ["Mongolia", "Siberia", "Ural", "Afghanistan", "India", "Siam"],
        "India": ["Middle East", "Afghanistan", "China", "Siam"],
        "Siam": ["India", "China", "Indonesia"],
        "Indonesia": ["Siam", "New Guinea", "Western Australia"],
        "New Guinea": ["Indonesia", "Western Australia", "Eastern Australia"],
        "Western Australia": ["Indonesia", "New Guinea", "Eastern Australia"],
        "Eastern Australia": ["New Guinea", "Western Australia"]
        }

        self.game_settings = GameSettings(2, "auto", "balanced_blitz", "static", True, False, False, "standard")

    
    def test_standard_init(self):
        territory_graph = TerritoryGraph(self.game_settings)
        self.assertEqual(territory_graph.territory_graph, self.standard_territory_graph)
        
    
    def test_erroneous_game_settings_type(self):
        with self.assertRaises(TypeError):
            territory_graph = TerritoryGraph(4)

    
    # Test is implied in game settings test
    def test_erroneous_game_settings_value(self):
        with self.assertRaises(ValueError):
            territory_graph = TerritoryGraph(GameSettings(2, "auto", "balanced_blitz", "static", True, False, False, "USA"))

    
    def test_get_neighbors_method(self):
        territory_graph = TerritoryGraph(self.game_settings)
        self.assertEqual(territory_graph.get_neighbors(Territory("Alaska", None, 0)), ["Northwest Territory", "Alberta", "Kamchatka"])

    
    def test_get_neighbors_method_erroneous_territory_type(self):
        territory_graph = TerritoryGraph(self.game_settings)
        with self.assertRaises(TypeError):
            territory_graph.get_neighbors(4)

    
    # Test is implied in territory test
    def test_get_neighbors_method_erroneous_territory_value(self):
        territory_graph = TerritoryGraph(self.game_settings)
        with self.assertRaises(ValueError):
            territory_graph.get_neighbors(Territory("Alaska", None, 1))

    
    