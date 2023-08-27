# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        head = root
        self.n = 0
        if root:
            self.visitNode(head, 0)
        return self.n

    def visitNode(self, node: Optional[TreeNode], n):
        # print (node,n)
        if (node):
            self.visitNode(node.left, n + 1)
            self.visitNode(node.right, n + 1)
        else:
            self.n = max(self.n, n)
