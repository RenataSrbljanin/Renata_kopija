scores = [87, 75, 75,75, 50, 32, 32]
ranks = []
for score in scores:
    ranks.append(scores.index(score) + 1)
print(ranks)