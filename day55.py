from math import comb

def surjections(n: int, k: int) -> int:
    total = 0
    for i in range(k + 1):
        total += (-1) ** i * comb(k, i) * (k - i) ** n
    return total
