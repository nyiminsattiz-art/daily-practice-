def find_missing_number(numbers):
    n = len(numbers) + 1
    return n * (n + 1) // 2 - sum(numbers)
