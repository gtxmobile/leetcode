from typing import Optional
from TreeNode import TreeNode
class Solution99:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.p1,self.p2,self.pre = None,None,None
        self.inorder(root)
        self.p1.val,self.p2.val = self.p2.val,self.p1.val

    def inorder(self,node):
        if not node:
            return None
        self.inorder(node.left)
        if self.pre is not None and self.pre.val>node.val:
            if not self.p1:
                self.p1= self.pre
            self.p2 = node
        self.pre = node
        self.inorder(node.right)
