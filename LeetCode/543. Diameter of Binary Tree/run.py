# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            l = root.left
            r = root.right
            return max(self.VisitNode(r) + self.VisitNode(l),
                       self.diameterOfBinaryTree(r), self.diameterOfBinaryTree(l))
        else:
            return 0

    def VisitNode(self, node):
        if node:
            return 1 + max(self.VisitNode(node.right), self.VisitNode(node.left))
        else:
            return 0
