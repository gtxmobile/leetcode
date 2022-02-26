class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        ret = []
        if root == None:
            return ret
        queue = [root]
        while queue:
            lq = len(queue)
            queue.append(None)
            for i in range(lq):
                n = queue.pop(0)
                n.next = queue[0]
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
            queue.pop(0)
        return root
