# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root and (root.left or root.right):
            l = root.left
            r = root.right
            r_l, flag_l = self.visitNode(l)
            r_r, flag_r = self.visitNode(r)
            if flag_l and flag_r:
                return abs(r_l - r_r) <= 1
            else:
                False
        else:
            return True

    def visitNode(self, node: Optional[TreeNode]) -> bool:

        if node:
            r = self.visitNode(node.right)
            l = self.visitNode(node.left)
            return 1 + max(r[0], l[0]), abs(r[0] - l[0]) <= 1 and r[1] and l[1]
        else:
            return 0, True
