class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        left = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:left+1],inorder[0:left])
        root.right = self.buildTree(preorder[left+1:],inorder[left+1:])
        return root