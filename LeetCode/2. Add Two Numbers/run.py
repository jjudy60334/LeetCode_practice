# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def IntTransform(self, l):
        n1 = l.val
        digit = 1
        str1 = l
        while str1.next:
            n1 += str1.next.val * (10**digit)
            str1 = str1.next
            digit += 1
        return n1

    def converIntListNode(self, number):
        number_list = [string for string in str(number)]
        l = ListNode(val=number_list[0])
        for n, i in enumerate(number_list):
            if n > 0:
                l = ListNode(val=i, next=l)
        return l

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n3 = self.IntTransform(l1) + self.IntTransform(l2)
        l3 = self.converIntListNode(n3)
        return l3
