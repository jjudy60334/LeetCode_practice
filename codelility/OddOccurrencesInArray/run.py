# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    count = {}
    for i in A:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    # print (count)
    return [i for i in count if count[i]%2 >0][0]