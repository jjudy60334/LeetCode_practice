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

    def insert(self, n, k, l, c):
        self.c = c
        if k <= n and l < n and l <= k:
            if k < n:
                self.left = Parent(self.value + "(")
                self.left.insert(n, k + 1, l, self.c)
            if l < k:
                self.right = Parent(self.value + ")")
                self.right.insert(n, k, l + 1, self.c)
            else:
                self.value = "("
        else:
            self.c.append(self.value)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        t = Parent()
        t.insert(n, 0, 0, [])
        return t.combination()
