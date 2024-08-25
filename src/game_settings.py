class GameSettings:
    possible_placement = {"auto", "semi_auto", "manuual"}
    possible_dice_rolls = {"balanced_blitz", "true_random"}
    possible_card_bonus_multiplier = {"static", "progressive"}
    possible_maps = {"standard"}

    # Assume classic world_domination gamemode for now
    def __init__(self, num_players, placement, dice_rolls, card_bonus_multiplier, is_blizzards, is_fog_of_war, is_portals, map):
        # Type checks
        if not isinstance(num_players, int):
            raise TypeError("Num players must be of type int")
        
        if not isinstance(placement, str):
            raise TypeError("Placement must be of type str")
        
        if not isinstance(dice_rolls, str):
            raise TypeError("Dice rolls must be of type str")
        
        if not isinstance(card_bonus_multiplier, str):
            raise TypeError("Card bonus multiplier must be of type str")
        
        if not isinstance(is_blizzards, bool):
            raise TypeError("Blizzards must be of type bool")
        
        if not isinstance(is_fog_of_war, bool):
            raise TypeError("Fog of war must be of type bool")
        
        if not isinstance(is_portals, bool):
            raise TypeError("Portals must be of type bool")
        
        if not isinstance(map, str):
            raise TypeError("Map must be of type str")
        

        # Attribute checks
        if num_players < 2 or num_players > 6:
            raise ValueError("Number of players must be between 2 and 6")
        
        if placement.lower() not in self.possible_placement:
            raise ValueError(f"Placement must be one of the following: {list(self.possible_placement)}")
        
        if dice_rolls.lower() not in self.possible_dice_rolls:
            raise ValueError(f"Dice rolls must be one of the following: {list(self.possible_dice_rolls)}")
        
        if card_bonus_multiplier.lower() not in self.possible_card_bonus_multiplier:
            raise ValueError(f"Card bonus muiltiplier must be one of the following: {list(self.possible_card_bonus_multiplier)}")
        
        if map.lower() not in self.possible_maps:
            raise ValueError(f"Map must be one of the following: {list(self.possible_maps)}")
        
        
        # Assignment
        self.num_players = num_players # /6
        self.placement = placement # auto, semi-auto, manual
        self.dice_rolls = dice_rolls # balanced blitz, true random
        self.card_bonus_multiplier = card_bonus_multiplier # static, progressive
        self.is_blizzards = is_blizzards # t/f
        self.is_fog_of_war = is_fog_of_war
        self.is_portals = is_portals
        self.map = map