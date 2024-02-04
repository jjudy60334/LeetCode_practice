# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # print ((Y-X))
    more_step = 1 if (Y-X) % D > 0 else 0
    return (Y-X)//D+more_step
