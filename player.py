import constants
import utils
from card import Card
from trick import Trick
from bot import Bot

class Player():
    def __init__(self, player_number: int, is_bot: bool):
        self.is_bot = is_bot
        if is_bot:
            self.bot = Bot()
        self.player_number = player_number
        self.hand = []
        self.points = 0

    def add_card(self, card: Card):
        self.hand.append(card)
        return card

    def remove_card(self, card: Card):
        self.hand.remove(card)
        return card
    
    def does_a_suit_match(self, card, cards):
        if card.is_trump and any(c.is_trump for c in cards):
            return True
        if not card.is_trump and any(c.suit == card.suit and not c.is_trump for c in cards):
            return True
        return False       
    
    def play_card(self, trick: Trick):
        legal_cards = []

        if trick.lead_card is not None and self.does_a_suit_match(trick.lead_card, self.hand):
            for card in self.hand:
                if trick.lead_card.is_trump:
                    if card.is_trump:
                        legal_cards.append(card)
                elif card.suit == trick.lead_card.suit and not card.is_trump:
                    legal_cards.append(card)
        else:
            legal_cards = self.hand

        if self.is_bot:
            selected_card = self.bot.choose_card(legal_cards)
        else:
            print("\nYou Have:")
            for card_number in range(len(self.hand)):
                text = f"{card_number + 1}: {self.hand[card_number].name}"
                print(text if self.hand[card_number] in legal_cards else utils.strikethrough(text))
            print("\nWhat card do you want to play?")
            card_played = False
            while not card_played:
                try:
                    selected_card = self.hand[int(input()) - 1]
                    if selected_card not in legal_cards:
                        raise(IndexError)
                    card_played = True
                except (ValueError, IndexError):
                    print("Invalid Selection. Please try again")

        trick.add_card(selected_card)
        self.remove_card(selected_card)

        print(f"Player {self.player_number} played {selected_card.name}")
    
    def add_trick(self, trick: Trick):
        trick_points = 0
        for card in trick.cards:
            trick_points += constants.RANK_POINTS.get(card.rank)
        
        self.points += trick_points

        return trick_points