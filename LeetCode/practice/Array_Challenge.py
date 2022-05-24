
def ArrayChallenge(arr):
    max_profit = 0
    min_v = min(arr)
    while (len(arr) > 1):
        min_v = min(arr)
        min_p = arr.index(min_v)
        if min_p + 1 < len(arr):
            max_profit = max(max(arr[min_p + 1:]) - min_v, max_profit)
        arr = arr[:min_p]
    return arr


print(ArrayChallenge(input()))
