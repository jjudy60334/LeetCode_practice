# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    b_k = (B)//K
    b_k = b_k
    a_k = A//K
    a_k = a_k-1 if A % K == 0 else a_k
    # print (b_k,a_k)
    ans = b_k-a_k
    return ans


# 87%
# [6, 11, 2]
# [6, 12, 2]
# [6, 11, 12]
# [6, 11, 11]
# [6, 13, 11]
# [6, 11, 8]
# [6, 11, 6]

# The following issues have been detected: wrong answers.

# For example, for the input [0, 0, 11] the solution returned a wrong answer (got 0 expected 1).

