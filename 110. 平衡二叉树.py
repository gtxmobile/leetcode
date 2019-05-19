class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if self.treeHeight(root)==-1:
            return False
        return True
    def treeHeight(self,root):
        if root==None:
            return 0
        lh=self.treeHeight(root.left)
        if lh==-1:
            return -1
        rh=self.treeHeight(root.right)
        if rh==-1:
            return -1
        hdiff=abs(lh-rh)
        if hdiff > 1:
            return -1
        else:
            return max(lh,rh)+1