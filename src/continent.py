from src.territory import Territory
class Continent:
    
    def __init__(self, name, territories, troop_bonus):
        # Type checks
        if not isinstance(name, str):
            raise TypeError("Continent name must be of type str")
        
        if not isinstance(territories, list):
            raise TypeError("Continent territories argument must be passed as a list of type Territory")

        for territory in territories:
            if not isinstance(territory, Territory):
                raise TypeError("Each territory in continent territories must be of type Territory")
            
        if not isinstance(troop_bonus, int):
            raise TypeError("Troop bonus must be of type int")
        

        # Attribute checks
        if not name:
            raise ValueError("Name cannot be empty")

        if troop_bonus < 0:
            raise ValueError("Troop bonus must be > 0")
        
        
        # Assignment
        self.name = name
        self.territories = territories
        self.troop_bonus = troop_bonus

    def occupied_by(self):
        pass