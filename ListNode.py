class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def generate(self,nums):
        dummy = ListNode(0)
        cur = dummy
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next

    def print(self, head):
        cur = head
        while cur:
            print(cur.val,end="-")
            cur = cur.next
        print("\n")
