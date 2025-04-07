import random

import constants
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in constants.RANKS for suit in constants.SUITS]
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards[-1]
        self.cards.pop(-1)
        return card