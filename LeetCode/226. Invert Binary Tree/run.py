# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        self.visitTree(head)
        return root

    def visitTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if (node):
            r = node.right
            l = node.left
            node.left = self.invertTree(r)
            node.right = self.invertTree(l)
        else:
            return None
