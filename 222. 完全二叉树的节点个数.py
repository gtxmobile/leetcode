from typing import Optional
from . import TreeNode


class Solution222:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ld = self.getDepth(root.left)
        rd = self.getDepth(root.right)
        if ld == rd:
            return (1 << ld) + self.countNodes(root.right)
        else:
            return (1 << rd) + self.countNodes(root.left)

    def getDepth(self, root):
        d = 0
        while root:
            d += 1
            root = root.left
        return d
