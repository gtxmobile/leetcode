from ListNode import ListNode
def swapPairs(head):
    if not head:
        return
    cur = head
    while cur and cur.next:
        tmp = cur.next.val
        cur.next.val = cur.val
        cur.val = tmp
        cur = cur.next.next
    return head

ln = []
for i in range(10):
    pr = None
    if i > 0:
        pr = ln[i - 1]
    ln.append(ListNode(i, pr))
n = ln[-1]
while n:
    # print n.val
    n = n.next
ret = swapPairs(ln[-1])
while ret:
    ret = ret.next
