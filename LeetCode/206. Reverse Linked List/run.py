# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ans_n = None

        while (head):
            ans_n = ListNode(head.val, ans_n)
            head = head.next

        return ans_n
