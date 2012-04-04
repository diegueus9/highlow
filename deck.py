COURTS = ['Spades', 'Hearts', 'Diamonds', 'Clubs'] 
SUITS = ['Ace', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

DECK = []

def init_deck():
    for court in COURTS:
        for suit in SUITS:
            DECK.append({'court': court, 'suit': suit})

def print_deck():
    for card in DECK:
        print "{suit} of {court}".format(court=card['court'], suit=card['suit'])


