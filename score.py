SCORE = 0
SCORE_INCREMENT_POINTS = 1
SCORE_DECREMENT_POINTS = -5

def increment_score():
    global SCORE, POINTS
    SCORE = SCORE + SCORE_INCREMENT
    POINTS = POINTS + 2

def decrement_score():
    global SCORE
    SCORE = SCORE - SCORE_DECREMENT

def print_score():
    print SCORE