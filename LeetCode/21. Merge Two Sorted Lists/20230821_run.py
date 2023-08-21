# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        result = ans
        while (list1 or list2):
            if list1 and not list2:
                val = list1.val
                list1 = list1.next

            elif list2 and not list1:
                val = list2.val
                list2 = list2.next
            elif list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            ans.next = ListNode(val=val)
            ans = ans.next

        return result.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        result = ans
        while (list1 and list2):
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            ans.next = ListNode(val=val)
            ans = ans.next
        if list1 or list2:
            ans.next = list1 if list1 else list2

        return result.next
