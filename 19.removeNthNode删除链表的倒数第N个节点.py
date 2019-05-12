
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


