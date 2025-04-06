from card import Card

class Player():
    def __init__(self):
        self.hand = []

    def add_card(self, card: Card):
        self.hand.append(card)

    def play_card(self, card: Card):
        self.hand.remove(card)
        return card