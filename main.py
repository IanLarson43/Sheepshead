import constants
from deck import Deck
from player import Player

deck = Deck()

players = [Player() for _ in range(constants.PLAYER_COUNT)]

p1 = players[0]
p2 = players[1]
p3 = players[2]
p4 = players[3]
p5 = players[4]

blind = []

for p in range(constants.PLAYER_COUNT):
    for c in range(constants.BASE_HAND_SIZE):
        players[p].add_card(deck.draw_card())
        # print(f"Player {p+1} drew {players[p].hand[c]}")

blind.append(deck.draw_card)
blind.append(deck.draw_card)

for hand in range(constants.BASE_HAND_SIZE):
    print("You Have:")
    for card_number in range(len(p1.hand)):
        print(f"{card_number+1}: {p1.hand[card_number]}")
    print("\nWhat card do you want to play?")

    card_played = False
    while not card_played:
        try:
            selected_card = p1.hand[int(input()) - 1]
            print(f"You selected {selected_card}")
            p1.play_card(selected_card)
            card_played = True
        except (ValueError, IndexError):
            print("Invalid Selection. Please try again")
