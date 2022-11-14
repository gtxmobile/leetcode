from typing import List


class Solution18:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n < 4:
            return ans
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                right = n - 1
                for k in range(j + 1, n - 1):
                    if k > j + 1 and nums[k - 1] == nums[k]:
                        continue
                    while k < right and nums[i] + nums[j] + nums[k] + nums[right] > target:
                        right -= 1
                    if k == right:
                        break
                    if nums[i] + nums[j] + nums[k] + nums[right] == target:
                        ans.append([nums[i], nums[j], nums[k], nums[right]])
        return ans
