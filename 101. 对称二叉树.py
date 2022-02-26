class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            lq = len(queue) - 1
            i = 0
            while i <= lq / 2:
                if queue[i] and queue[lq - i]:
                    if queue[i].val != queue[lq - i].val:
                        return False
                elif (queue[i] is None and queue[lq - i] is None):
                    pass
                else:
                    return False
                i += 1
            for i in range(lq + 1):
                n = queue.pop(0)
                if n:
                    queue.append(n.left)
                    queue.append(n.right)
        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        return self.comp(root, root)

    def comp(self, left, right):
        if left and right and left.val == right.val:
            return self.comp(left.left, right.right) and self.comp(left.right, right.left)
        elif not left and not right:
            return True
        else:
            return False
