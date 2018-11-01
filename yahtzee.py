import random
import operator
from collections import Counter

master_score_sheet = {
    "aces": " ", "twos": " ", "threes": " ", "fours": " ", 'fives': " ", 'sixes': " ", 'three_of_a_kind': " ",
    'four_of_a_kind': " ", "full_house": " ", "small_straight": " ", "large_straight": " ", "yahtzee": " ",
    "yahtzee_bonus": "  ", "chance": " ",
}

sub_totals = {
    'upper_bonus': ' ','upper_total': ' ', 'lower_total': ' ', 'grand_total': ' '
}

def diceroll(dice=1,sides=6):
    """Returns dice number of integers with sides number of sides. Defaults to 1 dice and 6 sides."""
    numbers = []
    for i in range(0,dice):
        numbers.append(random.randint(1,sides))
    return numbers




def chance(dice):
    """Calculates the Chance score. Adds up all dice."""
    return sum(dice)


def aces(dice):
    """Takes a list of dice values as input. It calculates the aces score."""
    return dice.count(1)

def twos(dice):
    """Takes a list of dice values as input. It calculates the twos score."""
    return dice.count(2) * 2

def threes(dice):
    """Takes a list of dice values as input. It calculates the threes score."""
    return dice.count(3) * 3

def fours(dice):
    """Takes a list of dice values as input. It calculates the fours score."""
    return dice.count(4) * 4

def fives(dice):
    """Takes a list of dice values as input. It calculates the fives score."""
    return dice.count(5) * 5

def sixes(dice):
    """Takes a list of dice values as input. It calculates the sixes score."""
    return dice.count(6) * 6


def three_of_a_kind(dice):
    """Calculates three of a kind score. If there are 3 of the same dice, adds up total of all dice."""
    z = Counter(dice)
    for k, v in z.items():
        if v > 2:
            return sum(dice)
    return 0


def four_of_a_kind(dice):
    """Calculates four of a kind score. If there are 4 of the same dice, adds up total of all dice."""
    z = Counter(dice)
    for k, v in z.items():
        if v > 3:
            return sum(dice)
    return 0


def full_house(dice):
    """Calculates full hour score. If there is a three of a kind and two of a kind returns 25."""
    for die in dice:
        if dice.count(die)==3:
            for die in dice:
                if dice.count(die)==2:
                    return 25
    return 0


def small_straight(dice):
    """Calculates small straight score."""
    sd = sorted(dice)
    first_sraight = True
    second_straight = True
    for i in range(2):
        if sd[i+1] != sd[i] + 1:
            first_sraight = False
    for i in range(1,3):
        if sd[i+1] != sd[i]  + 1:
            second_straight = False
    if first_sraight & second_straight:
        return 30
    else:
        return 0


def large_straight(dice):
    """Calculates large straight score."""
    sd = sorted(dice)
    for i in range(3):
        if sd[i+1] != sd[i]  + 1:
            return 0
    return 40


def yahtzee(dice):
    """Calculates yahtzee score. If all dice are the same number, returns 50."""
    z = Counter(dice)
    for k, v in z.items():
        if v > 4:
            return 50
    return 0


def yahtzee_bonus(dice):
    """Calculates yahtzee score. If all dice are the same number, returns 50."""
    z = Counter(dice)
    for k, v in z.items():
        if v > 4:
            return 100
    return 0


def chooser(dice, master_score_sheet):
    """Determines which of the unused scores will be highest. Takes a list of dice values and the list of available
    items."""
    hundies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
    func_dictionary = {"aces": aces(dice), "twos": twos(dice), "threes": threes(dice), "fours": fours(dice),
    "fives": fives(dice), "sixes": sixes(dice), "three_of_a_kind": three_of_a_kind(dice),
    "four_of_a_kind": four_of_a_kind(dice), "full_house":full_house(dice), "small_straight": small_straight(dice),
    "large_straight": large_straight(dice), "yahtzee": yahtzee(dice), "yahtzee_bonus": yahtzee_bonus(dice),
    "chance": chance(dice)}
    for k, v in master_score_sheet.items():
        if master_score_sheet[k] != " " and master_score_sheet[k] not in hundies:
            del func_dictionary[k]
    highest_scorer = max(func_dictionary.items(), key=operator.itemgetter(1))[0]
    if highest_scorer == "yahtzee":
        master_score_sheet["yahtzee_bonus"] = " "
    if highest_scorer == "yahtzee_bonus" and master_score_sheet["yahtzee_bonus"] != " ":
        func_dictionary[highest_scorer] = master_score_sheet[highest_scorer] + 100
    return (highest_scorer, func_dictionary[highest_scorer])


def display_score_sheet(master_score_sheet):
    """Prints out a display of the score sheet. Takes value from the dictionary master_score_sheet."""
    print(
        f"""
Upper Section
Aces: {master_score_sheet["aces"]}
Twos: {master_score_sheet["twos"]}
Threes: {master_score_sheet["threes"]}
Fours: {master_score_sheet["fours"]}
Fives: {master_score_sheet["fives"]}
Sixes: {master_score_sheet["sixes"]}
Bonus: {sub_totals['upper_bonus']}
Upper Section Total: {sub_totals['upper_total']}

Lower Section
3 of a kind: {master_score_sheet['three_of_a_kind']}
4 of a kind: {master_score_sheet['four_of_a_kind']}
Full House: {master_score_sheet['full_house']}
Small Straight: {master_score_sheet['small_straight']}
Large Straight: {master_score_sheet['large_straight']}
Yahtzee: {master_score_sheet['yahtzee']}
Chance: {master_score_sheet['chance']}
Yahtzee Bonus: {master_score_sheet['yahtzee_bonus']}


        """
    )


def most_common(lst):
    return max(set(lst), key=lst.count)


def turn_dice():
    """Simulates taking three dice rolls. Each time keeping the most common dice."""
    # first dice roll
    dice = diceroll(5)
    # second dice roll
    keepers = most_common(dice)
    dice = [keepers] * dice.count(keepers)
    new_dice = diceroll(5-len(dice))
    for d in new_dice:
       dice.append(d)
    # third dice roll
    keepers = most_common(dice)
    dice = [keepers] * dice.count(keepers)
    new_dice = diceroll(5-len(dice))
    for d in new_dice:
       dice.append(d)
    return dice


def scoring_test():
    just1 = [1, 1, 1, 1, 1]
    just2 = [2, 2, 2, 2, 2]
    just3 = [3, 3, 3, 3, 3]
    just4 = [4, 4, 4, 4, 4]
    just5 = [5, 5, 5, 5, 5]
    just6 = [6, 6, 6, 6, 6]
    one_five = [1, 2, 3, 4, 5]
    d32 = [3, 3, 3, 2, 2]

    assert aces(just1) == 5
    assert aces(just5) == 0
    assert aces(one_five) == 1
    assert twos(just2) == 10
    assert twos(just3) == 0
    assert threes(just3) == 15
    assert threes(one_five) == 3
    assert fours(just4) == 20
    assert fours(just6) == 0
    assert fives(just5) == 25
    assert fives(just6) == 0
    assert sixes(just6) == 30
    assert sixes(just5) == 0

    assert three_of_a_kind(one_five) == 0
    assert three_of_a_kind(d32) == 13
    assert four_of_a_kind(d32) == 0
    assert four_of_a_kind([1, 1, 1, 1, 5]) == 9
    assert full_house(d32) == 25
    assert full_house(one_five) == 0
    assert small_straight(one_five) == 30
    assert small_straight(d32) == 0
    assert large_straight(one_five) == 40
    assert large_straight(just5) == 0
    assert yahtzee(just5) == 50
    assert yahtzee(d32) == 0
    assert chance(just1) == aces(just1)
    assert chance(one_five) == 15
    assert yahtzee_bonus(d32) == 0
    assert yahtzee_bonus(just3) == 100


scoring_test()

