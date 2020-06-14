class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        if root:
            self.push_stack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack.pop()
        if top.right:
            self.push_stack(top.right)
        return top.val

    def push_stack(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
