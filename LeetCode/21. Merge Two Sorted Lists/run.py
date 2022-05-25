# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lst1 = list1
        lst2 = list2
        list3 = ListNode() if lst1 or lst2 else None
        l3 = list3
        while lst1 or lst2:

            l3.val = min([i.val for i in [lst1, lst2] if i])

            if lst1 and lst1.val == l3.val:
                lst1 = lst1.next
            elif lst2:
                lst2 = lst2.next
            l3.next = ListNode() if lst1 or lst2 else None
            l3 = l3.next

        return list3
