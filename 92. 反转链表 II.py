class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head:
            return
        stack=[]
        qian=hou=head
        prv=None
        i=1
        while i<m:
            prv=qian
            qian=qian.next
            i+=1
        hou=qian
        while i<=n:
            stack.append(hou)
            hou=hou.next
            i+=1
        while stack:
            if not prv:
                prv=stack.pop()
                head=prv
            else:
                prv.next=stack.pop()
                prv=prv.next
        prv.next=hou
        return head