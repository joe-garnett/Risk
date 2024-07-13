class Player:
    possible_colors = {"red", "yellow", "blue", "purple", "orange", "green", "pink"}


    def __init__(self, name, color) -> None:
        # Type checks
        if not isinstance(name, str):
            raise TypeError("Player name must be of type string")

        if not isinstance(color, str):
            raise TypeError("Player color must be of type string")


        # Lowercase for consistency
        color = color.lower()
        

        # Attribute uniqueness
        if self.color not in self.possible_colors:
            raise ValueError(f"Player color must be one of the following: {list(self.possible_colors)}")

        
        # Assignment
        self.name = name  
        self.color = color
