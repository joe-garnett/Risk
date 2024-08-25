from src.territory import Territory
from src.player import Player
from src.continent import Continent

class Board:

    def __init__(self, continents, territory_graph):
        # Type checks
        if not isinstance(continents, list):
            raise TypeError("Board continents must be of type list")
        
        for continent in continents:
            if not isinstance(continent, Continent):
                raise TypeError("Each continent in board continents must be of type Continent")
        
        if not isinstance(territory_graph, dict):
            raise TypeError("Board territory graph must be of type dict")
        
        # Todo check if territory graph is valid - maybe add a method for this?
        # Could use netwrkx to check if graph is connected
        # make territory graph a class
        
    
        # Assignment
        self.continents = continents
        self.territory_graph = territory_graph
    