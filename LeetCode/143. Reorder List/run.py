# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while( fast and fast.next and fast.next.next):
            # print (slow,fast)
            slow=slow.next
            fast=fast.next.next

        sec=slow
        pre=None
        # print ('sec',sec)
        while(sec):
            temp=sec.next
            sec.next=pre
            pre=sec
            sec=temp
        # print ('sec,pre',sec,pre)

        ##merge
        first=head
        second=pre
        
        while( second and first):
            tmp=first.next
            first.next=second
            first=first.next
            second = second.next
            first.next=tmp
            first=first.next
            