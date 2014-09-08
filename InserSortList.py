# Definition for singly-linked list.
from random import randint

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    # @param head, a ListNode
    # @return a ListNode
def sortList(head):
    cur = head

    ite = cur
    while cur:

    while head:
        a.append(head)
        head=head.next
    a.sort(key=my_cmp)
    prv=a[0]

    for ai in a[1::]:
        prv.next=ai
        prv=ai
    ai.next=None
    ai=a[0]
    while ai:
        print ai.val
        ai=ai.next

root=ListNode(1)
prv=root
for i in range(10):
    n=ListNode(randint(1,100))
    prv.next=n
    prv=n

sortList(root)



