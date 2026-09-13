def f(n: int, m: int) -> int:
    full_cycle = n // m
    cycle_sum = (m * (m - 1) / 2)
    remain_sum = (n % m) * (n % m + 1) / 2
    return full_cycle * cycle_sum + remain_sum


