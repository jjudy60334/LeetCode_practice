# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not (self.isSame(root.right, subRoot) or self.isSame(root.left, subRoot) or self.isSame(root, subRoot)):
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        else:
            return True

    def isSame(self, r1, r2):
        if not r1 and not r2:
            return True
        elif r1 and r2:
            return r1.val == r2.val and self.isSame(r1.right, r2.right) and self.isSame(r1.left, r2.left)
        else:
            return False
