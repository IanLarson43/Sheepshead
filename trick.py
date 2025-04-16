import constants
from card import Card

class Trick:
    def __init__(self):
        self.cards = []
        self.lead_card = None

    def add_card(self, card: Card):
        if self.cards == []:
            self.lead_card = card
        self.cards.append(card)
        return card
    
    def evaluate_winner(self):
        card_scores = [constants.CARD_STRENGTH.get(card.name) for card in self.cards]

        for card_index in range(constants.PLAYER_COUNT):
            card = self.cards[card_index]
            if card.suit != self.lead_card.suit and not card.is_trump:
                card_scores[card_index] = 0

        largest_score_index = card_scores.index(max(card_scores))
        return self.cards[largest_score_index]
        
