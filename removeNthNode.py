
def removeNthFromEnd(head, n):
        qian=head
        if not head.next:
            return None
        while n>0:
            qian=qian.next
            n-=1
        if not qian:
            return head.next
        cur=head
        while qian.next:
            cur=cur.next
            qian=qian.next
        print cur.val
        cur.next=cur.next.next
        return head
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    # @param head, a ListNode
    # @return a ListNode

from random import randint
root=ListNode(1)
prv=root
for i in range(1,5):
    for j in range(randint(0,3)):
        n=ListNode(i)
        prv.next=n
        prv=n

def deleteDuplicates(head):
        prv=head.val
        cur=head.next
        while cur:
            if cur.val==prv:
                #print cur.val
                cur=cur.next.next
            else:
                prv.next=cur
                prv=cur
                cur=cur.next
        return head
cur=root
while cur:
    print cur.val
    cur=cur.next
print '*'*100
cur=deleteDuplicates(root)
while cur:
    print cur.val
    cur=cur.next

