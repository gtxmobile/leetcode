class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        p = None
        cur = head
        while cur:
            p, cur.next, cur = cur, p, cur.next
        return p
