class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a list node
    # @return a tree node
    def tomid(self, head, l, h):
        if l > h:
            return None, head
        mid = l + ((h - l) >> 1)
        left, head = self.tomid(head, l, mid - 1)
        root = TreeNode(head.val)
        root.left = left
        head = head.next
        root.right, head = self.tomid(head, mid + 1, h)
        return root, head

    def sortedListToBST(self, head):
        p = head
        l = 0
        while p:
            l += 1
            p = p.next
        ret, _ = self.tomid(head, 0, l - 1)
        return ret
