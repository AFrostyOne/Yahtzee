import yahtzee as y
import copy
import matplotlib.pyplot as plt
import statistics as st


def play_game():
    master_score_sheet = copy.deepcopy(y.master_score_sheet)
    for i in range(13):
        dice = y.turn_dice()
        turn_results = y.chooser(dice, master_score_sheet)
        master_score_sheet[turn_results[0]] = turn_results[1]
    total_score = 0
    for k, v in master_score_sheet.items():
        if isinstance(v, int):
            total_score += v
    return total_score


scores = []
for i in range(10000):
    scores.append(play_game())

print(scores)
print("Mean:",st.mean(scores))
print("Median", st.median(scores))
print("Standard Deviation:", st.stdev(scores))
print("Min:", min(scores))
print("Max", max(scores))

plt.show(plt.hist(scores, bins=200))
