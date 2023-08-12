class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        char_dic={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for n,c in enumerate(s):
            if c in char_dic:
                if len(stack)>0 and stack[-1]==char_dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) 
            # print (c,stack)
        return True if stack==[] else False               