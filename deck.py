COURTS = ['Spades', 'Hearts', 'Diamonds', 'Clubs'] 
COURTS = ['Spades', 'Hearts',] 
SUITS = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
SUITS = ['Ace', 2, 3, 'Jack', 'Queen', 'King']

DECK = []

def init_deck():
    for court in COURTS:
        for suit in SUITS:
            DECK.append({'court': court, 'suit': suit})

def print_deck():
    for card in DECK:
        print_card(card)

def print_card(card):
    print "Card: {suit} of {court}".format(court=card['court'], suit=card['suit'])

def print_remaining_cards():
    print "Remaining cards: {remaining_cards}".format(remaining_cards=len(DECK))