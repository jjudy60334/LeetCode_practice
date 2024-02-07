# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    stack = [0] * len(A)
    for a in A:
        if a > len(A):
            return 0
        else:
            stack[a-1] = 1
    return 1 if sum(stack) ==len(A) else 0