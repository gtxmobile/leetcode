# Definition for singly-linked list.
from random import randint

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    # @param head, a ListNode
    # @return a ListNode
def my_cmp(s):
    return s.val
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        a=[]
        while head:
            a.append(head)
            head=head.next
        if a:
            a.sort(key=my_cmp)
            prv=a[0]
            for ai in a[1::]:
                prv.next=ai
                prv=ai
            prv.next=None
            return a[0]
        else:
            return None



