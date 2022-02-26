# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head: return False
        n1 = head
        n2 = head

        while n2 and n2.next:
            n2 = n2.next.next
            n1 = n1.next
            if n1 == n2:
                return True
        return False
