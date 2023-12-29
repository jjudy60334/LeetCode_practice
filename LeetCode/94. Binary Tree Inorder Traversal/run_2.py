# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        self.ans = []
        self.visit(root)
        return self.ans

    def visit(self, root):
        if not root:
            return
        left = root.left
        right = root.right

        self.visit(left)
        self.ans.append(root.val)
        self.visit(right)
