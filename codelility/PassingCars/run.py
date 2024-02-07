# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    ans = 0
    sum_q = sum(A)
    for a in A:
        if a == 0:
            ans += sum_q
        else:
            sum_q -= 1
        if sum_q <= 0:
            return ans
        if ans >= 10**9:
            return -1
    return ans
