# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q):
            return self.visitNode(p, q)
        else:
            return not p and not q

    def visitNode(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            # print (p,q, self.visitNode(p.left,q.left),self.visitNode(p.right,q.right))
            if p.val == q.val:
                return True and self.visitNode(p.left, q.left) and self.visitNode(p.right, q.right)
            else:
                return False
        else:
            return not p and not q

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class SecondSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        if p and q and p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
