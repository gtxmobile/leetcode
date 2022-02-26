class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum) | self.hasPathSum(root.right, sum)
