# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.run = {}
        self.visit(root, 0)
        return self.run.values()

    def visit(self, root, level):
        if not root:
            return
        # print (root.val)
        if level not in self.run:
            self.run[level] = [root.val]
        else:
            self.run[level].append(root.val)
        self.visit(root.left, level+1)
        self.visit(root.right, level+1)
