import time

import constants
from deck import Deck
from player import Player
from trick import Trick

players = [Player(1, False)] + ([Player(_ + 2, True) for _ in range(constants.PLAYER_COUNT - 1)])

while True:
    deck = Deck()
    blind = []
    round_players = players

    for p in range(constants.PLAYER_COUNT):
        for c in range(constants.BASE_HAND_SIZE):
            players[p].add_card(deck.draw_card())

    blind.append(deck.draw_card)
    blind.append(deck.draw_card)

    for hand in range(constants.BASE_HAND_SIZE):
        trick = Trick()

        time.sleep(constants.TEXT_DELAY)
        round_players[0].play_card(trick)
        time.sleep(constants.TEXT_DELAY)
        round_players[1].play_card(trick)
        time.sleep(constants.TEXT_DELAY)
        round_players[2].play_card(trick)    
        time.sleep(constants.TEXT_DELAY)
        round_players[3].play_card(trick)
        time.sleep(constants.TEXT_DELAY)
        round_players[4].play_card(trick)
        time.sleep(constants.TEXT_DELAY)

        winning_card = trick.evaluate_winner()
        winner_index = trick.cards.index(winning_card)
        winner = round_players[winner_index]
        round_players[winner_index].add_trick(trick)

        print(f"\nWinner is Player {winner.player_number}\n")

        round_players[:] = round_players[winner_index:] + round_players[:winner_index]

    for p in range(constants.PLAYER_COUNT):
        print(f"Player {players[p].player_number} had {players[p].points} points")
        time.sleep(constants.TEXT_DELAY)
    time.sleep(constants.TEXT_DELAY)
    print("\n\n\n\n\n")
    time.sleep(constants.TEXT_DELAY)
    players[:] = players[1:] + players[:1]