# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return head
        kuai=head
        man=head
        prv=None
        while kuai and kuai.next:
            prv=man
            man=man.next
            kuai=kuai.next.next
        #翻转后半条
        prv.next=None
        prv=None
        mid=man
        while mid:
            tmp=mid.next
            mid.next=prv
            prv=mid
            mid=tmp
        fan=prv
        zheng=head
        root=head
        while zheng and fan:
            tmp1=zheng.next
            tmp2=fan.next
            zheng.next=fan
            if tmp1:
                fan.next=tmp1
            zheng=tmp1
            fan=tmp2
        return root




