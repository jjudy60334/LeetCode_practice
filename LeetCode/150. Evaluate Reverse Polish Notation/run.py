class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        # print (tokens)
        for i in tokens:
            if i in operators:
                # print (i,stack)
                if stack:
                    string = eval(stack[-2] + i + stack[-1])
                    stack = stack[:-2]
                    stack.append(str(int(string)))
            else:
                stack.append(i)
        return int(stack[0])

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","-","*","/"]
        # print (tokens)
        for i in tokens:
            if i in operators:
                if i=="+":
                    string=stack[-2]+stack[-1]
                if i=="-":
                    string=stack[-2]-stack[-1]
                if i=="*":
                    string=stack[-2]*stack[-1]
                if i=="/":
                    string=int(stack[-2]/stack[-1])
                stack=stack[:-2]
                stack.append(int(string))
            else:
                stack.append(int(i))
        return int(stack[0])