# Definition for singly-linked list.
from random import randint

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def my_cmp(s):
    return s.val
    # @param head, a ListNode
    # @return a ListNode
def sortList(head):
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

root=ListNode(1)
prv=root
for i in range(10):
    n=ListNode(randint(1,100))
    prv.next=n
    prv=n

#sortList(root)


