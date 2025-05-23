import constants

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        
        self.name = f"{rank} of {suit}"
        self.points = constants.RANK_POINTS.get(rank, None)
        self.is_trump = (rank in constants.TRUMP_RANKS) or (suit == "Diamonds")

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit