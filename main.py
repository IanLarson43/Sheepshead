import time

import constants
from deck import Deck
from player import Player
from bot import Bot
from trick import Trick

deck = Deck()

players = [Player() for _ in range(constants.PLAYER_COUNT)]
bots = [Bot() for _ in range(constants.PLAYER_COUNT - 1)]

p1 = players[0]

p2 = players[1]
p2_bot = bots[0]

p3 = players[2]
p3_bot = bots[1]

p4 = players[3]
p4_bot = bots[2]

p5 = players[4]
p5_bot = bots[3]

blind = []

for p in range(constants.PLAYER_COUNT):
    for c in range(constants.BASE_HAND_SIZE):
        players[p].add_card(deck.draw_card())
        # print(f"Player {p+1} drew {players[p].hand[c]}")

blind.append(deck.draw_card)
blind.append(deck.draw_card)

for hand in range(constants.BASE_HAND_SIZE):
    print("\nYou Have:")
    for card_number in range(len(p1.hand)):
        print(f"{card_number + 1}: {p1.hand[card_number].name}")
    print("\nWhat card do you want to play?")

    card_played = False
    while not card_played:
        try:
            selected_card = p1.hand[int(input()) - 1]
            print(f"You played {selected_card.name}")
            trick = Trick(p1.play_card(selected_card))
            card_played = True
        except (ValueError, IndexError):
            print("Invalid Selection. Please try again")

    time.sleep(constants.TEXT_DELAY)
    print(f"Player 2 played {trick.add_card(p2.play_card(p2_bot.choose_card(p2.hand))).name}")
    time.sleep(constants.TEXT_DELAY)
    print(f"Player 3 played {trick.add_card(p3.play_card(p3_bot.choose_card(p3.hand))).name}")
    time.sleep(constants.TEXT_DELAY)
    print(f"Player 4 played {trick.add_card(p4.play_card(p4_bot.choose_card(p4.hand))).name}")
    time.sleep(constants.TEXT_DELAY)
    print(f"Player 5 played {trick.add_card(p5.play_card(p5_bot.choose_card(p5.hand))).name}")
    time.sleep(constants.TEXT_DELAY)

    print(trick.evaluate_winner().name)