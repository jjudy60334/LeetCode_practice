class Parent:
    def __init__(self, value=""):
        self.left = None
        self.right = None
        self.c = []
        self.value = value

    def combination(self):
        return self.c

    def left(self, node):
        self.left = node

    def right(self, node):
        self.right = node

    def get_data(self, c):
        self.c = c
        if self.left or self.right:
            if self.left:
                self.left.get_data(self.c)
            # print (self.value),
            if self.right:
                self.right.get_data(self.c)
        else:
            print(self.value)
            self.c.append(self.value)
            return self.c

    def insert(self, n, k, l):

        if k <= n and l < n and l <= k and (k == n and l == n) == False:
            if k + 1 <= n:
                self.left = Parent(self.value + "(")
                self.left.insert(n, k + 1, l)
            if l < k:
                self.right = Parent(self.value + ")")
                self.right.insert(n, k, l + 1)
            else:
                self.data = "("


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        t = Parent()
        t.insert(n, 0, 0)
        t.get_data([])
        return t.combination()
