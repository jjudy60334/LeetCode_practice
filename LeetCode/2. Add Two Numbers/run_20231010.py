# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        head = ListNode(val=0)
        ans = head
        while (l1 or l2):
            n += l1.val if l1 else 0
            n += l2.val if l2 else 0
            ans.val = n % 10
            n = n // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            next_ans = ListNode(val=n) if (n > 0 or l1 or l2) else None
            ans.next = next_ans
            ans = ans.next
        return head
