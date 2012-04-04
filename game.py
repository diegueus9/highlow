from random import randint

from deck import DECK, SUITS

def first_card():
    return next_card()

def next_card():
    card = DECK.pop(randint(0, len(DECK)-1))
    return card

def is_higher(current_card, last_card):
    if SUITS.index(last_card['suit']) > SUITS.index(current_card['suit']):
        return True
    else:
        return False

def user_is_right(current_card, last_card, higher_lower):
    print current_card, last_card, higher_lower
    if is_higher(current_card, last_card) and higher_lower=="higher":
        return True
    elif not is_higher(current_card, last_card) and higher_lower=="lower":
        return True
    else:
        return False
    