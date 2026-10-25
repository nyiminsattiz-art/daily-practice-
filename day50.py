from itertools import combinations

def choose_best_sum(t, k, ls):
    best_sum = None
    
    for combo in combinations(ls, k):
        current_sum = sum(combo)
        
        if current_sum <= t:
            if best_sum is None or current_sum > best_sum:
                best_sum = current_sum
    return best_sum
