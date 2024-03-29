class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution21:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(-1)
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if not l1:
            cur.next = l2
        if not l2:
            cur.next = l1
        return head.next
