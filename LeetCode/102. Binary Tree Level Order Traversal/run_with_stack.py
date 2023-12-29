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
        l = 0
        stack = [(root, l)]
        run = {l: [root.val]}
        while stack != []:
            head = stack.pop(0)
            h, l = head
            # print (h,l)
            if l+1 not in run:
                run[l+1] = []
            if h.left:
                stack.append((h.left, l+1))
                run[l+1].append(h.left.val)
            if h.right:
                stack.append((h.right, l+1))
                run[l+1].append(h.right.val)
        return [i for i in run.values() if i !=[]]