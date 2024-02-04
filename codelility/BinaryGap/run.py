# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    b = find_binary(N)
    # print (b)
    l = [n for n, k in enumerate(str(b)) if k == '1']
    # +[len(str(b))]
    # print ('l',l)
    ans = 0
    if len(l) <= 1:
        return 0
    for i in range(len(l)-1):
        ans = max([ans, l[i+1]-l[i]])
    return ans-1


def find_binary(i):
    if not i:
        return 0
    k = 0
    while (i//(2**k) > 1):
        k += 1

    return 10**k+find_binary(i % (2**k))
