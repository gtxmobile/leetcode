import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        root = ListNode(-1)
        cur = root
        small = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(small, (lists[i].val, i))
        while small:
            _, i = heapq.heappop(small)
            cur.next = lists[i]
            cur = cur.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(small, (lists[i].val, i))
        return root.next
