from collections import Counter

def score(dice):
    TRIPLE = {1 : 1000, 2 : 200, 3 : 300, 4 : 400, 5 : 500, 6 : 600}
    SINGLE = {1 : 100, 5 : 50}
    total = 0
    for face, count in Counter(dice).items():
        total += (count // 3) * TRIPLE[face]
        total += (count % 3) * SINGLE.get(face, 0)
    return total
