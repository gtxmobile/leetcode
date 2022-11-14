from typing import List


class Solution31:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                j = i
                while j < l and nums[i - 1] < nums[j]:
                    j += 1
                nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
                break
            i -= 1
        nums[i:] = sorted(nums[i:])


nums = [1,2,3]
Solution31().nextPermutation(nums)
print(nums)
