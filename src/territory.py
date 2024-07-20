from src.player import Player

class Territory:
    def __init__(self, name, occupied_by=None, num_troops=0):
        # Type checks
        if not isinstance(name, str):
            raise TypeError("Territory name must be of type string")
        
        if occupied_by is not None and not isinstance(occupied_by, Player):
            raise TypeError("Territory occupier must be of type Player or None")
        
        if not isinstance(num_troops, int):
            raise TypeError("Number of troops in a territory must be of type integer")


        # Attribute validation
        if occupied_by is None and num_troops > 0:
            raise ValueError("Territory cannot have troops and be unoccupied")

        if occupied_by and num_troops <= 0:
            raise ValueError("Territory cannot be occupied with < 1 troop")


        # Assignment
        self.name = name
        self.occupied_by = occupied_by
        self.num_troops = num_troops

    # Maybe introduce getters and setters but may be too verbose for now