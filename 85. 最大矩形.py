from typing import List
class Solution85:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        self.ans = 0
        heights = [[0]*n for _ in range(m)]
        for i in range(m):
            for j,v in enumerate(matrix[i]):
                if i ==0:
                    heights[i][j] = int(v)
                elif v == "0":
                    heights[i][j] = 0
                else:
                    heights[i][j] = 1+heights[i-1][j]

        for h in heights:
            help(h)
        return self.ans

    def help(self,height):
        stack=[]
        height.append(0)
        for l,h in enumerate(height):
            while stack and height[stack[-1]]>h:
                idx = stack.pop()
                self.ans = max(self.ans, height[idx]*(l if not stack else l-stack[-1]-1))
            stack.append(l)

