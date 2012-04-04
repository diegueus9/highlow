from deck import DECK, init_deck, print_card, print_remaining_cards
from game import first_card, next_card, user_is_right
from score import increment_score, decrement_score, print_current_score, print_final_score, \
    print_increment_points, print_decrement_points

def init_game():
    init_deck()

def play():
    higher_lower = None
    current_card = first_card()
    print_remaining_cards()
    print_current_score()
    print_card(current_card)
    while len(DECK)>0:
        while higher_lower != 'higher' and higher_lower != 'lower':
            print
            higher_lower = raw_input("The next card is higher or lower? (higher/lower) ")
        last_card = next_card()
        if user_is_right(current_card, last_card, higher_lower):
            print
            print 'Right!'
            print_increment_points()
            increment_score()
            print
        else:
            print
            print 'Wrong :('
            print_decrement_points()
            decrement_score()
            print
        print_remaining_cards()
        print_current_score()
        print_card(last_card)

        # print current_card, last_card
        # kind of reset
        current_card = last_card
        higher_lower = None

    print
    print "Goodbye!"
    print_final_score()

if __name__ == "__main__":
    init_game()
    play()