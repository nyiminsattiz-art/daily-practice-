def sum_of_differences(arr):
    if len(arr) <= 1:
        return 0
    else:
        result = 0
        arr = sorted(arr, reverse=True)
        for i in range(len(arr) - 1):
            result += arr[i] - arr[i + 1]
    return result
