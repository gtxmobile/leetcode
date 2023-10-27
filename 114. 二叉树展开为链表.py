from typing import Optional
from TreeNode import TreeNode


class Solution114:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.help(root)

    def help(self, root):
        if not root:
            return None
        self.help(root.right)
        self.help(root.left)
        root.right = self.pre
        root.left = None
        self.pre = root
