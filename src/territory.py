
class Territory:
    def __init__(self, name, occupied_by=None, num_troops=0):
        self.name = name 
        self.occupied_by = occupied_by
        self.num_troops = num_troops

        if self.occupied_by is None and self.num_troops > 0:
            raise ValueError("Territory cannot have troops and be unoccupied")
        
        if self.occupied_by and self.num_troops <= 0:
            raise ValueError("Territory cannot be occupied with < 1 troop")
        


        