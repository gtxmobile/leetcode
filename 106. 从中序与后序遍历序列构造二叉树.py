class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])

        left = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:left], postorder[0:left])
        root.right = self.buildTree(inorder[left + 1:], postorder[left:-1])
        return root
