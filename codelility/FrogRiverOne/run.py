# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    stack = [0]*X
    sum_stack = 0
    for n, a in enumerate(A):
        if stack[a-1] == 0:
            sum_stack += 1
            stack[a-1] = 1
        if sum_stack == X:
            return n
    return -1
