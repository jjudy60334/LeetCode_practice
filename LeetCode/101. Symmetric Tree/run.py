# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.visit(root.left, root.right)

    def visit(self, l, r):
        if not l or not r:
            return not l and not r
        return self.visit(l.left, r.right) and self.visit(l.right, r.left) and l.val == r.val
