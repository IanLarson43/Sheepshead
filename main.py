import time

import constants
from deck import Deck
from player import Player
from trick import Trick

deck = Deck()

players = [Player(1, False)] + ([Player(_ + 2, True) for _ in range(constants.PLAYER_COUNT - 1)])

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
    trick = Trick()

    p1.play_card(trick)
    time.sleep(constants.TEXT_DELAY)
    p2.play_card(trick)
    time.sleep(constants.TEXT_DELAY)
    p3.play_card(trick)    
    time.sleep(constants.TEXT_DELAY)
    p4.play_card(trick)
    time.sleep(constants.TEXT_DELAY)
    p5.play_card(trick)
    time.sleep(constants.TEXT_DELAY)

    print(trick.evaluate_winner().name)