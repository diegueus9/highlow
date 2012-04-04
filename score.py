SCORE = 0
SCORE_INCREMENT_POINTS = 1
SCORE_DECREMENT_POINTS = 5

def increment_score():
    global SCORE, SCORE_INCREMENT_POINTS
    SCORE = SCORE + SCORE_INCREMENT_POINTS
    SCORE_INCREMENT_POINTS = SCORE_INCREMENT_POINTS + 2

def decrement_score():
    global SCORE, SCORE_DECREMENT_POINTS
    SCORE = SCORE - SCORE_DECREMENT_POINTS

def print_current_score():
    print "Current score: {score}".format(score=SCORE)

def print_final_score():
    print "Final score: {score}".format(score=SCORE)

def print_increment_points():
    print "+{points} points".format(points=SCORE_INCREMENT_POINTS)

def print_decrement_points():
    print "-{points} points".format(points=SCORE_DECREMENT_POINTS)