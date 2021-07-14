class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_f = ""
        comma = ""
        flage = 0
        for n, sub in enumerate(s):
            # print (s,string_f,sub,sub.isdigit(),flage)
            if sub in ("+", "-") and len(comma) == 0 and flage == 0:
                comma += sub
            elif sub.isdigit():
                string_f += sub
                flage = 1
            elif flage == 0 and len(comma) > 0:
                break

            elif string_f == "" and sub == " ":
                pass

            else:
                break
        print(string_f, string_f.isdigit(), flage, flage == 0 or not string_f.isdigit())
        if (flage == 0 or not(string_f.isdigit())):
            return 0
        string_f = int(comma + string_f)
        b_u = -2**31
        b_f = 2**31 - 1
        # print (b_f)
        if max(b_u, string_f) == b_u:
            return b_u
        elif min(b_f, string_f) == b_f:
            return b_f
        else:
            return string_f
