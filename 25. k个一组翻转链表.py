class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution25:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head or k < 2:
            return head
        dummy = ListNode(-1)
        cur = head
        head = dummy
        tail = cur
        while cur:
            cnt = k
            while cnt and tail:
                tail = tail.next
                cnt -= 1
            if cnt > 0:
                dummy.next = cur
                break
            else:
                prv = tail
                prvtail = cur
                while not cur == tail:
                    tmp = cur.next
                    cur.next = prv
                    prv = cur
                    cur = tmp
                dummy.next = prv
                dummy = prvtail
        return head.next
