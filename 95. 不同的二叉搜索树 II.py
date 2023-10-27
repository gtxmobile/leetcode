from TreeNode import TreeNode
from typing import List,Optional
class Solution95:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen(start, end):
            if start>end:
                return [None,]
            ans = []
            for i in range(start, end+1):
                lt = gen(start,i-1)
                rt = gen(i+1,end)

                for l in lt:
                    for r in rt:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        ans.append(cur)
            return ans
        return gen(1,n)