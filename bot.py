import random

import constants

class Bot:
    def __init__(self):
        pass

    def choose_card(self, hand):
        return random.choice(hand) # TODO: Make this have real logic
    
    def choose_pick(self, player):
        choice = random.choice([True, False])
        return choice # TODO: Make this have real logic
    
    def bury(self, player):
        for i in range(constants.BLIND_SIZE):
            player.bury(random.randint(0, len(player.hand) - 1))
