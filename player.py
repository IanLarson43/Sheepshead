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
    
    def play_card(self, trick: Trick):
        if self.is_bot:
            selected_card = self.bot.choose_card(self.hand)
        else:
            print("\nYou Have:")
            for card_number in range(len(self.hand)):
                print(f"{card_number + 1}: {self.hand[card_number].name}")
            print("\nWhat card do you want to play?")
            card_played = False
            while not card_played:
                try:
                    selected_card = self.hand[int(input()) - 1]
                    
                    card_played = True
                except (ValueError, IndexError):
                    print("Invalid Selection. Please try again")

        trick.add_card(selected_card)
        self.remove_card(selected_card)

        print(f"Player {self.player_number} played {selected_card.name}")