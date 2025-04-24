import time

import constants
import utils
from deck import Deck
from player import Player
from trick import Trick
from card import Card

players = [Player(1, False)] + ([Player(_ + 2, True) for _ in range(constants.PLAYER_COUNT - 1)])

while True:
    deck = Deck()
    blind = []
    round_players = players

    for p in range(constants.PLAYER_COUNT):
        for c in range(constants.BASE_HAND_SIZE):
            players[p].add_card(deck.draw_card())

    for i in range(constants.BLIND_SIZE):
        blind.append(deck.draw_card())

    time.sleep(constants.TEXT_DELAY)
    for p in players:
        if p.is_bot:
            print(f"Player {p.player_number}'s turn to pick")
            time.sleep(constants.TEXT_DELAY)
            if p.bot.choose_pick(p):
                p.hand += blind
                p.is_picker = True
                p.bot.bury(p)
                print("They pick")
                break
            else:
                print("They pass")
        else:
            print("It's your turn to pick")
            time.sleep(constants.TEXT_DELAY)
            print("\nYou Have:")
            for card_number in range(len(p.hand)):
                text = f"{card_number + 1}: {p.hand[card_number].name}"
                print(text)
            time.sleep(constants.TEXT_DELAY)
            print("\nWould you like to pick? (y/n)")
            pick_choosen = False
            while not pick_choosen:
                pick_choice = input().casefold()
                if pick_choice == "y":
                    p.hand += blind
                    p.is_picker = True
                    print("You pick")
                    time.sleep(constants.TEXT_DELAY)
                    print("\nYou Have:")
                    for card_number in range(len(p.hand)):
                        text = f"{card_number + 1}: {p.hand[card_number].name}"
                        print(text)
                    print("\n")
                    time.sleep(constants.TEXT_DELAY)
                    print("What card would you like to call?")
                    time.sleep(constants.TEXT_DELAY)
                    callable_cards = []
                    for suit in constants.FAIL_SUITS:
                        ace = Card("Ace", suit)
                        if utils.suit_matches(ace, p.hand) and not any(ace == c for c in p.hand):
                            callable_cards.append(ace)
                    for card_number in range(len(callable_cards)):
                        print(f"{card_number + 1}: {callable_cards[card_number].name}")
                    card_called = False
                    while not card_called:
                        try:
                            called_card = callable_cards[int(input()) - 1]
                            card_called = True
                        except (ValueError, IndexError):
                            print("Invalid Selection. Please try again")
                    called_suit_cards = [card for card in p.hand if card.suit == called_card.suit]

                    for i in range(constants.BLIND_SIZE):
                        time.sleep(constants.TEXT_DELAY)
                        print("\nYou Have:")
                        for card_number in range(len(p.hand)):
                            text = f"{card_number + 1}: {p.hand[card_number].name}"
                            is_illegal_bury = utils.only_and_matching_card(p.hand[card_number], called_suit_cards)
                            print(utils.strikethrough(text) if is_illegal_bury else text)
                        time.sleep(constants.TEXT_DELAY)
                        print("\nWhat card would you like to bury?")
                        card_buried = False
                        while not card_buried:
                            try:
                                bury_card_number = int(input()) - 1
                                if utils.only_and_matching_card(p.hand[bury_card_number], called_suit_cards):
                                    raise IndexError # Is this really a good way to do this?
                                p.bury(bury_card_number)
                                card_buried = True
                            except (ValueError, IndexError):
                                print("Invalid Selection. Please try again")
                    pick_choosen = True
                elif pick_choice == "n":
                    print("You pass")
                    pick_choosen = True
                else:
                    print("Invalid Selection. Please try again")
            if pick_choice == "y":
                break

    for h in range(constants.BASE_HAND_SIZE):
        trick = Trick()

        time.sleep(constants.TEXT_DELAY)

        for p in range(constants.PLAYER_COUNT):
            round_players[p].play_card(trick)
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