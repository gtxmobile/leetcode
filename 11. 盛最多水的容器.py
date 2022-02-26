class Solution:
    # @return an integer
    def maxArea(self, height):
        area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = max(area, (r - l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
