# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.visit(root) >= 0

    def visit(self, root):
        if not root:
            return 0
        l_h, r_h = self.visit(root.left), self.visit(root.right)
        if l_h < 0 or r_h < 0 or abs(l_h-r_h) > 1:
            return -1
        return max(l_h, r_h)+1
