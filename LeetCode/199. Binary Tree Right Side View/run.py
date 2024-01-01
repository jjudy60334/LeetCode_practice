# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = {}
        self.visit(root, 0)
        # print (self.ans)
        return [i[0] for i in self.ans.values()]

    def visit(self, root, level):
        if not root:
            return None
        if level not in self.ans:
            self.ans[level] = [root.val]
        if root.right:
            self.visit(root.right, level+1)
        if root.left:
            self.visit(root.left, level+1)
