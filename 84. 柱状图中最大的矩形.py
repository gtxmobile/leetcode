from typing import List
class Solution84:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights.append(0)
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                idx = stack.pop()
                ans = max(ans,heights[idx] *(i if not stack else i-stack[-1]-1))
            stack.append(i)
        return ans