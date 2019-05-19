# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        zuo=ListNode(-1)
        you=ListNode(-1)
        zroot=zuo
        yroot=you
        cur=head
        while cur:
            if cur.val<x:
                zuo.next=cur
                zuo=cur
            else:
                you.next=cur
                you=cur
            cur=cur.next
        you.next=None
        zuo.next=yroot.next
        return zroot.next
