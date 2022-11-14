from typing import List


class Solution15:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n < 3:
            return ans
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            right = n - 1
            for left in range(i + 1, n - 1):
                if left > i + 1 and nums[left - 1] == nums[left]:
                    continue
                while left < right and nums[left] + nums[right] > target:
                    right -= 1
                if left == right:
                    break
                if nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])
        return ans
