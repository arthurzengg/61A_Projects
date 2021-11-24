"""
    This file contains your final_strategy that will be submitted to the contest.

    You can only depend on "general-purpose" libraries - do not import or open any
    contest-specific files, like other Python or text files. All contest logic must
    be in this file.

    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = 'King Arthur'  # Change this line!


def final_strategy(score, opponent_score):
    if opponent_score != 0:
        if score == 0:
            return picky_piggy_strategy(score, opponent_score, cutoff = 8, num_rolls = 5)
        else:
            return hog_pile_strategy(score, opponent_score, cutoff = 8, num_rolls = 5)
    else:
        if score == 0:
            return 0
        else:
            return 5


    """if score >= 100 - 10 and score > opponent_score:
        return hog_pile_strategy(score, opponent_score, 3, 1)

    if score > opponent_score and opponent_score > 100 / 2:
        return hog_pile_strategy(score, opponent_score, 11, 5)

    return hog_pile_strategy(score, opponent_score, 10, 6) """

def hog_pile_strategy(score, opponent_score, cutoff=8, num_rolls=5):

    zero_roll_score = score + picky_piggy(opponent_score)
    if hog_pile(zero_roll_score, opponent_score):
        if opponent_score >= zero_roll_score:
            return 0
        else:
            return num_rolls
    return picky_piggy_strategy(score, opponent_score, cutoff, num_rolls)

def picky_piggy(score):

    index = score
    if (score == 0):
        return 7
    else:
        while(index >= 6):
            index = score % 6
        if index == 1:
            return 1
        elif index == 2:
            return 4
        elif index == 3:
            return 2
        elif index == 4:
            return 8
        elif index == 5:
            return 5
        elif index == 0:
            return 7

def hog_pile(player_score, opponent_score):

    if (player_score != opponent_score):
        return 0
    else:
        return opponent_score

def picky_piggy_strategy(score, opponent_score, cutoff=8, num_rolls=5):

    if picky_piggy(opponent_score) >= cutoff:
        return 0
    return num_rolls
