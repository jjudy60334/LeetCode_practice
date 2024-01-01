# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        h = root
        self.visit(root)
        return h

    def visit(self, root):
        if not root:
            return None
        tmp = root.right
        root.right = root.left if root.left else None
        root.left = tmp if tmp else None
        self.visit(root.left)
        self.visit(root.right)
