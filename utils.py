def strikethrough(text):
    return f"\033[9m{text}\033[0m"

def suit_matches(card, cards):
        if card.is_trump and any(c.is_trump for c in cards):
            return True
        if not card.is_trump and any(c.suit == card.suit and not c.is_trump for c in cards):
            return True
        return False   

def only_and_matching_card(card, cards): # TODO: Rename?
    return len(cards) == 1 and card == cards[0]