PLAYER_COUNT = 5

BASE_HAND_SIZE = 6

BLIND_SIZE = 2

TEXT_DELAY = 0.5

RANK_POINTS = {
    "7": 0, "8": 0, "9": 0,
    "King": 4,
    "10": 10,
    "Ace": 11,
    "Jack": 2,
    "Queen": 3
}

TRUMP_RANKS = {
    "Jack", "Queen"
}

CARD_STRENGTH = {
    "7 of Hearts": 1, "7 of Spades": 1, "7 of Clubs": 1,
    "8 of Hearts": 2, "8 of Spades": 2, "8 of Clubs": 2,
    "9 of Hearts": 3, "9 of Spades": 3, "9 of Clubs": 3,
    "King of Hearts": 4, "King of Spades": 4, "King of Clubs": 4,
    "10 of Hearts": 5, "10 of Spades": 5, "10 of Clubs": 5,
    "Ace of Hearts": 6, "Ace of Spades": 6, "Ace of Clubs": 6,
    "7 of Diamonds": 7, 
    "8 of Diamonds": 8, 
    "9 of Diamonds": 9, 
    "King of Diamonds": 10, 
    "10 of Diamonds": 11, 
    "Ace of Diamonds": 12, 
    "Jack of Diamonds": 13,
    "Jack of Hearts": 14,
    "Jack of Spades": 15,
    "Jack of Clubs": 16,
    "Queen of Diamonds": 17,
    "Queen of Hearts": 18,
    "Queen of Spades": 19,
    "Queen of Clubs": 20
}

RANKS = ["7", "8", "9", "King", "10", "Ace", "Jack", "Queen"]
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
FAIL_SUITS = ["Clubs", "Spades", "Hearts"]