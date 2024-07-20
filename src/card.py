class Card:
    # comprising forty-two territory cards, two wild cards
    # check if this is the same in the online risk 
    
    # should add the "territory" of the card if necessary.
    # number of territory cards depend on the map i think - assume standard for now 
    card_types = {"infantry", "cavalry", "artillery", "wild"}
    def __init__(self, card_type):
        # Type checks
        if not isinstance(card_type, str):
            raise TypeError("Card type must be of input type str")


        # Attribute validation
        if card_type.lower() not in self.card_types:
            raise ValueError("Invalid territory card")
        

        # Assignment
        self.type = card_type