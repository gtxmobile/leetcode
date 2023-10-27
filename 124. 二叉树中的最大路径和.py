from typing import Optional
from TreeNode import TreeNode


class Solution124:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -100000
        self.depthSum(root)
        return self.ans

    def depthSum(self, root):
        if not root:
            return 0
        ret = root.val
        lv = self.depthSum(root.left)
        rv = self.depthSum(root.right)
        if lv > 0:
            ret += lv
        if rv > 0:
            ret += rv
        self.ans = max(self.ans, ret)
        tmp = max(lv, rv)
        return tmp + root.val if tmp > 0 else root.val
