import json
from src.territory import Territory
from src.game_settings import GameSettings

class TerritoryGraph:
    def __init__(self, game_settings):
        # Type checks
        if not isinstance(game_settings, GameSettings):
            raise TypeError("Game settings must be of type GameSettings")
        
        self.territory_graph = self.get_territory_graph(game_settings.map)


    def get_territory_graph(self, map_name):
        # Type checks
        if not isinstance(map_name, str):
            raise TypeError("Map name must be of type str")
        
        
        try:
            with open(f"src/data/territory_graphs.json") as file:
                data = json.load(file)
                
                if map_name not in data:
                    raise ValueError(f"Map name must be one of the following: {list(data.keys())}")
                
                return data[map_name]
    
        except FileNotFoundError:
            raise FileNotFoundError("The territory graph file 'src/data/territory_graphs.json' does not exist.")
    
        except json.JSONDecodeError:
            raise ValueError("The territory graph file is not a valid JSON file.")
        

    # As territories will be validated in the game settings, this method will not need to be validated
    def get_neighbors(self, territory):
        # Type checks
        if not isinstance(territory, Territory):
            raise TypeError("Territory must be of type Territory")
        
        return self.territory_graph[territory.name]