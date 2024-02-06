# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    ans = [0]*N
    max_v = 0
    for a in A:
        if a <= N:
            ans[a-1] += 1
            max_v = ans[a-1] if max_v < ans[a-1] else max_v
        else:
            ans = [max_v]*N
    return ans
