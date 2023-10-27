class Solution113:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum) | self.hasPathSum(root.right, sum)
