# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    stack = [0]*(len(A)+1)
    for a in A:
        # print (a,stack)
        stack[a-1] = 1
    return [n+1 for n, s in enumerate(stack) if s == 0][0]
