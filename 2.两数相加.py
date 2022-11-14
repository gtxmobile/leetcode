# coding:utf-8
from ListNode import ListNode
class Solution2(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        ret = ListNode(-1)
        cur = ret
        while l1 or l2 or c > 0:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            he = n1 + n2 + c
            cur.next = ListNode(he %10)
            c = he // 10
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ret.next

ln = ListNode(1)
l1 = ln.generate([1,2,3])
l2 = ln.generate([4,5,6])
he = Solution2().addTwoNumbers(l1,l2)
ln.print(he)

