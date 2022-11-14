from typing import List


class Solution41:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            n = nums[i]
            while 0 < n <= l and nums[n - 1] != n:
                nums[n - 1],n = n,nums[n-1]
        for i,n in enumerate(nums):
            if n != i+1:
                return i+1
        return len(nums)+1

print(Solution41().firstMissingPositive([3,4,-1,1]))