from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.index(nums,target)
        right = self.index(nums[::-1],target)
        if right > -1:
            right = len(nums)-right
        return [left,right]

    def index(self, a, x):
        'Locate the leftmost value exactly equal to x'
        i = bisect.bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        return -1

print(Solution().searchRange([5,7,7,8,8,10],7))