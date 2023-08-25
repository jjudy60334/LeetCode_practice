# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pin = head
        i = 0
        while (pin):
            pin = pin.next
            i += 1
        k = 0
        pin = head
        if i - n == 0:
            pin2 = head.next
            return pin2
        while (i - n >= k):
            if i - n == k + 1:
                nxt = pin.next
                pin.next = nxt.next
            else:
                pin = pin.next
            k += 1
        return head
