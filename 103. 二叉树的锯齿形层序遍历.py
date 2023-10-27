from typing import Optional,List
from TreeNode import TreeNode
class Solution103:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return []
        left = 1
        level = []
        level.append(root)
        while level:
            tmp =[]
            l = len(level)
            while l:
                node = level.pop(0)
                tmp.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                l-=1
            ans.append(tmp[::left])
            left = -left




