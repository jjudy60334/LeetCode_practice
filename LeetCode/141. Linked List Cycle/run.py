# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ans = head
        collect = []
        while ans:
            collect.append(ans)
            ans = ans.next
            if ans in collect:
                return True
        return False
