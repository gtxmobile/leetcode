from typing import Optional
from TreeNode import  TreeNode
class Solution98:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, l=float('-inf'), r=float('inf')):
            if not node:
                return True
            return node.value>l and node.value<r and isValid(node.left,l,node.val) \
                   and isValid(node.right,node.value,r)
        return isValid(root)