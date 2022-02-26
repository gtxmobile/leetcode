# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        self.ret = 0
        self.gui(root, 0)
        return self.ret

    def gui(self, root, acc):
        if not root.left and not root.right:
            self.ret += acc * 10 + root.val
        else:
            if root.left:
                self.gui(root.left, acc * 10 + root.val)
            if root.right:
                self.gui(root.right, acc * 10 + root.val)
