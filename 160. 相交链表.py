# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        curA = headA
        curB = headB

        while curA != curB:
            if not curA:
                curA = headB
            else:
                curA = curA.next
            if not curB:
                curB = headA
            else:
                curB = curB.next
        return curA


        