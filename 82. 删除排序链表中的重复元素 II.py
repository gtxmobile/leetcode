# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return None
        cur=head
        head=ListNode(-1)
        prv=head
        dup=False
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur=cur.next
                dup=True
            elif dup:
                cur=cur.next
                dup=False
            else:
                prv.next=cur
                prv=cur
                cur=cur.next
        if dup:
            prv.next=None
        else:
            prv.next=cur
        return head.next