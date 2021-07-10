class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        tail = 1
        s = str(s)

        # if s_len<2:
        #     return s_len
        distinct_string = dict()
        max = 0
        f = 0
        appear_once = 0
        for n, i in enumerate(s):
            if i not in distinct_string.keys():
                distinct_string[i] = [n]
            else:
                # print (n,distinct_string[i][-1])
                # length=n-distinct_string[i][-1]
                max = n - appear_once if n - appear_once > max else max
                print(n - appear_once, n, appear_once, s[n], s[appear_once])
                appear_once = distinct_string[i][-1] + 1
                distinct_string[i].append(n)

                f = 1
                # max = length if length>max else max

            print(n, distinct_string[i], i, max, s[appear_once], appear_once, len(s))
        max = len(s) - appear_once if len(s) - appear_once > max else max
        if f == 0:
            max = len(s)

        # print (distinct_string,max)
        # while  tail<len(s):
        #     if s[tail] not in distinct_string:
        #         distinct_string[s[tail]]=tail
        #         tail+=1
        #     else :
        #         n=distinct_string[s[tail]]+1
        #         distinct_string[s[n]]=[n]
        #         tail=n+1
        #     if s_len-n <max:
        #         break

            # length=len(distinct_string)
            # # print (s[n:tail],n,tail,s[n],s[tail],length,max,s_len-n)
            # max = length if length>max else max
        return max
