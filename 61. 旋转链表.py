# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        kuai=head
        man=head
        if not head:
            return None
        cur=head
        cnt=0
        while cur:
            cnt+=1
            cur=cur.next
        k%=cnt
        for i in range(k):
            kuai=kuai.next
        if kuai==None:
            return head
        while kuai.next:
            man=man.next
            kuai=kuai.next
        kuai.next=head
        head=man.next
        man.next=None
        return head

